from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('threads/', thread_list, name='threads-list'),
    path('threads/<int:id>/', thread_detail, name='thread-detail'),
    path('threads/create', create_thread, name='thread-create'),
    path('threads/<int:id>/delete/', delete_thread, name='thread-delete'),
    path('threads/<int:id>/edit/', edit_thread, name='thread-edit' ),
    path('threads/<int:id>/create_post/', create_post, name='post-create'),
    path('posts/<int:id>/delete/', delete_post, name='post-delete'),
]