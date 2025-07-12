#!/usr/bin/env python3
"""
Setup script for StackIt project
This script helps with initial project setup and database configuration
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("✗ Python 3.8 or higher is required")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def check_postgresql():
    """Check if PostgreSQL is available"""
    try:
        result = subprocess.run(['psql', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ PostgreSQL detected")
            return True
        else:
            print("✗ PostgreSQL not found. Please install PostgreSQL first.")
            return False
    except FileNotFoundError:
        print("✗ PostgreSQL not found. Please install PostgreSQL first.")
        return False

def setup_database():
    """Setup PostgreSQL database"""
    print("\nSetting up database...")
    
    # Create database
    create_db_cmd = "psql -U postgres -c 'CREATE DATABASE stackit_db;'"
    if not run_command(create_db_cmd, "Creating database"):
        print("Database might already exist, continuing...")
    
    # Grant privileges
    grant_cmd = "psql -U postgres -c \"GRANT ALL PRIVILEGES ON DATABASE stackit_db TO postgres;\""
    run_command(grant_cmd, "Granting privileges")

def setup_django():
    """Setup Django project"""
    print("\nSetting up Django...")
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        return False
    
    # Make migrations
    if not run_command("python manage.py makemigrations", "Creating migrations"):
        return False
    
    # Run migrations
    if not run_command("python manage.py migrate", "Running migrations"):
        return False
    
    # Create superuser
    print("\nCreate a superuser account (optional):")
    create_superuser = input("Do you want to create a superuser? (y/n): ").lower().strip()
    if create_superuser == 'y':
        run_command("python manage.py createsuperuser", "Creating superuser")
    
    return True

def main():
    """Main setup function"""
    print("StackIt Setup Script")
    print("=" * 50)
    
    # Check prerequisites
    if not check_python_version():
        return False
    
    if not check_postgresql():
        print("\nPlease install PostgreSQL and try again.")
        return False
    
    # Setup database
    setup_database()
    
    # Setup Django
    if not setup_django():
        return False
    
    print("\n" + "=" * 50)
    print("✓ Setup completed successfully!")
    print("\nTo start the development server, run:")
    print("python manage.py runserver")
    print("\nThen open http://127.0.0.1:8000 in your browser")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 