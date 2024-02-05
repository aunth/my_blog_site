
from django.shortcuts import render
from post_app.views import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
