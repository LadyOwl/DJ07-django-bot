from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('user/', views.get_user_info, name='get_user_info'),
]