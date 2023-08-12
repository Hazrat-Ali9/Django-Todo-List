from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add_task/',views.TaskFormView.as_view(), name='add_task'),
    path('show_tasks/',views.ShowTaskView.as_view(), name='show_tasks'),
    path('completed_tasks/',views.CompletedTaskView.as_view(), name='completed_tasks'),
    path('edit_task/<int:pk>',views.TaskUpdateView.as_view(), name='edit_task'),
    path('delete_task/<int:pk>',views.TaskDeleteView.as_view(), name='delete_task'),
    path('com_delete_task/<int:pk>',views.Completed_pageTaskDeleteView.as_view(), name='completed_delete_task'),
    path('complete_task/<int:id>',views.CompleteTaskUpdate, name='complete_task'),
]
