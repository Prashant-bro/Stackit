from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Question
import json

def home(request):
    """Home page view"""
    questions = Question.objects.all().order_by('-created_at')
    context = {
        'questions': questions
    }
    return render(request, 'index.html', context)

def question_list(request):
    """API endpoint to get all questions"""
    questions = Question.objects.all().order_by('-created_at')
    data = []
    for question in questions:
        data.append({
            'id': question.id,
            'title': question.title,
            'description': question.description,
            'tags': question.tags,
            'username': question.user.username,
            'created_at': question.created_at.strftime('%Y-%m-%d %H:%M'),
            'answer_count': 0  # You can add answer count logic later
        })
    return JsonResponse(data, safe=False)

@login_required
def ask_question(request):
    """View for asking a new question"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tags = request.POST.get('tags', '')
        
        if title and description:
            question = Question.objects.create(
                user=request.user,
                title=title,
                description=description,
                tags=tags
            )
            return redirect('question_detail', question_id=question.id)
    
    return render(request, 'ask.html')

def question_detail(request, question_id):
    """View for displaying a specific question"""
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question
    }
    return render(request, 'question_detail.html', context)

@csrf_exempt
def create_question_api(request):
    """API endpoint to create a new question"""
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user if request.user.is_authenticated else None
        
        if not user:
            return JsonResponse({'status': 'error', 'message': 'User not authenticated'}, status=401)
        
        title = data.get('title')
        description = data.get('description')
        tags = data.get('tags', '')
        
        if title and description:
            question = Question.objects.create(
                user=user,
                title=title,
                description=description,
                tags=tags
            )
            return JsonResponse({
                'status': 'success',
                'message': 'Question created successfully',
                'question_id': question.id
            })
        else:
            return JsonResponse({'status': 'error', 'message': 'Title and description are required'}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)
