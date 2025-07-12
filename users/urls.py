from django.urls import path
from .views import login_view, login_api, register_api, logout_view, profile_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('login/api/', login_api, name='login_api'),
    path('register/api/', register_api, name='register_api'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]