from . import views as base_views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', base_views.home_view, name='home'),
	path('contact/', base_views.contact_view, name='contact'),
	path('about/', base_views.about_view, name='about'),
    path('terms_and_condition/', base_views.TermsAndConditionView.as_view(), name='terms_and_condition'),
]
