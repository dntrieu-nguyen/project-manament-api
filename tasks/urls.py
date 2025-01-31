from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>/', get_task_by_id),  # Sử dụng <str:id>
    path('', get_tasks_by_project_id),
    path('create', create_task),
    path('update', update_task),
    path('delete', delete_task),
    path('send-invite', send_invite_join_task),
    path('accept', accept_invitation),
    path('decline', decline_invitation),
]
