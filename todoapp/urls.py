from django.urls import path
from todoapp.views import *

urlpatterns = [
    path('todos/', TodoListCreateView.as_view(), name='todo-list'),
    path('todos/<int:id>/', TodoDetailView.as_view(), name='todo-detail'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]