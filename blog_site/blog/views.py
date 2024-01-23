from django.views import generic
from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    
    def render_to_response(self, context, **response_kwargs):
        print(context)  # Add this line to print context
        return super().render_to_response(context, **response_kwargs)


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': posts})

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to the home page or any desired page
        else:
            print(form.errors)
            print("Your form is not correct")
    else:
        print("Not post method")
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


class TermsAndConditionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'terms_and_condition.html')