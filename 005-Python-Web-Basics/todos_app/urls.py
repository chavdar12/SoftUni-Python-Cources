from django.urls import path

from todos_app.views import index, create_task, edit_task, delete_task, do_task

urlpatterns = [
    path('', index, name='todo index'),
    path('create/', create_task, name='create task'),
    path('edit/<int:pk>', edit_task, name='edit todo'),
    path('delete/<int:pk>', delete_task, name='delete todo'),
    path('do_task/<int:pk>', do_task, name='do task')
]

