from django.urls import path
from user_app import views as user_views
from django.contrib.auth import views as auth_views
from .views import login_view

urlpatterns = [
	path('profile/', user_views.profile_view, name='profile'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),	
	path('login/', login_view, name='login'),
]
