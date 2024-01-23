from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.PostList.as_view(), name='home'),
    path('', views.register, name='register'),
    path('terms_and_condition/', views.TermsAndConditionView.as_view(), name='terms_and_condition'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
