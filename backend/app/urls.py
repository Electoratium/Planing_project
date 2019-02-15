from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
	path('create-user', createUser, name='create-user'),
	path('check-token', checkToken, name='check-token'),
	path('api-token-auth', login, name='login'),
	path('planing/get-day-tasks', get_day_tasks, name='get_day_tasks'),
]