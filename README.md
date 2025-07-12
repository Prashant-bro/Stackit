<<<<<<< HEAD
# StackIt - Q&A Platform

A Django-based question and answer platform similar to Stack Overflow.

## Features

- User authentication (login/register)
- Ask and view questions
- User profiles
- PostgreSQL database
- Responsive design

## Setup Instructions

### Prerequisites

1. Python 3.8 or higher
2. PostgreSQL database
3. pip (Python package manager)

### Database Setup

1. Install PostgreSQL on your system
2. Create a new database:
   ```sql
   CREATE DATABASE stackit_db;
   CREATE USER postgres WITH PASSWORD 'postgres';
   GRANT ALL PRIVILEGES ON DATABASE stackit_db TO postgres;
   ```

### Project Setup

1. Navigate to the project directory:
   ```bash
   cd Stackit
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Open your browser and go to `http://127.0.0.1:8000`

## Project Structure

```
Stackit/
├── stackit_project/     # Django project settings
├── users/              # User authentication app
├── questions/          # Questions app
├── answers/            # Answers app (future)
├── votes/              # Voting app (future)
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Usage

1. **Home Page**: View all questions
2. **Login/Register**: Create an account or sign in
3. **Ask Question**: Create new questions (requires login)
4. **View Questions**: Click on any question to see details
5. **Profile**: View your profile and questions

## API Endpoints

- `GET /` - Home page
- `GET /questions/` - Get all questions (JSON)
- `POST /api/questions/` - Create new question
- `GET /users/login/` - Login page
- `POST /users/login/api/` - Login API
- `POST /users/register/api/` - Register API
- `GET /users/profile/` - User profile (requires login)

## Database Configuration

The project is configured to use PostgreSQL with the following default settings:
- Database: `stackit_db`
- User: `postgres`
- Password: `postgres`
- Host: `localhost`
- Port: `5432`

You can modify these settings in `stackit_project/settings.py`.

## Development

To add new features:

1. Create new Django apps: `python manage.py startapp app_name`
2. Add models in `app_name/models.py`
3. Create views in `app_name/views.py`
4. Add URL patterns in `app_name/urls.py`
5. Include app URLs in main `urls.py`
6. Run migrations: `python manage.py makemigrations && python manage.py migrate`

## Troubleshooting

1. **Database Connection Error**: Make sure PostgreSQL is running and the database exists
2. **Static Files Not Loading**: Run `python manage.py collectstatic`
3. **Migration Errors**: Delete `db.sqlite3` and run migrations again
4. **Port Already in Use**: Use `python manage.py runserver 8001` for different port

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License. 
=======
#StackIt – A Minimal Q&A Forum Platform 
Overview 
StackIt is a minimal question-and-answer platform that supports collaborative 
learning and structured knowledge sharing. It’s designed to be simple, user-friendly, 
and focused on the core experience of asking and answering questions within a 
community


Team name- Eklavya
1)Prashant Singh
email-prashantsingh20102006@gmail.com
2)Jinit shah
email-shahjinit52@gmail.com
3)Lavya Yadav
email-lavyayadav07@gmail.com
4)Ankit Patel
email-apatel97771@gmail.com

>>>>>>> 70324a22421d0352be31b80829f560b0e574a424
