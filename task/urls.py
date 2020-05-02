from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name="api-over-view"),
    path('task-list/', views.taskList, name='task-list'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:id>', views.taskDelete, name='task-delete'),
]