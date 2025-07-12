from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def login_view(request):
    """Login page view"""
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')

@csrf_exempt
def login_api(request):
    """API endpoint for login"""
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "success", "message": "Logged in successfully"})
        else:
            return JsonResponse({"status": "fail", "message": "Invalid credentials"}, status=401)
    return JsonResponse({"status": "error", "message": "Only POST allowed"}, status=400)

@csrf_exempt
def register_api(request):
    """API endpoint for user registration"""
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "error", "message": "Username already exists"}, status=400)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({"status": "error", "message": "Email already exists"}, status=400)
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return JsonResponse({"status": "success", "message": "User registered successfully"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    
    return JsonResponse({"status": "error", "message": "Only POST allowed"}, status=400)

@login_required
def logout_view(request):
    """Logout view"""
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    """User profile view"""
    user_questions = request.user.question_set.all().order_by('-created_at')
    context = {
        'user': request.user,
        'questions': user_questions
    }
    return render(request, 'profile.html', context)

