from . import views as base_views
from django.urls import path
from post_app import views as post_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('create_post/', post_views.create_post, name='create_post'),
    path('post_detail/<int:pk>/', post_views.post_detail, name='post_detail'),
]
