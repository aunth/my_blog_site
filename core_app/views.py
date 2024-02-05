from django.views import generic
from django.shortcuts import render, redirect
from post_app.models import Post
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


FIELD_FOR_SORTING_MAP = {
    'Likes': 'likes',
    'Time':'-created_on'
}


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

def about_view(request):
    # Your view logic goes here
    return render(request, 'about.html') 

def contact_view(request):
    return render(request, 'contact.html')


def picked_theme(request):
    print(request.GET)
    if 'theme' in request.GET:
        return request.GET.get('theme')
    else:
        return False

def home_view(request):
    theme = picked_theme(request)
    print(theme)
    if theme:
        posts = Post.objects.filter(theme=theme)
    else:
        posts = Post.objects.all()

    # Get the selected sorting options from the request
    selected_sort = request.GET.getlist('sort_by', default=['Time'])

    # Validate selected_sort to avoid potential security risks
    selected_sort = [option for option in selected_sort if option in FIELD_FOR_SORTING_MAP]

    # Apply sorting to posts based on the selected options
    posts = posts.order_by(FIELD_FOR_SORTING_MAP[selected_sort[0]])

    available_themes = Post._meta.get_field('theme').choices

    themes = [theme[1] for theme in available_themes]

    context = {
        'posts': posts,
        'sort_options': FIELD_FOR_SORTING_MAP.keys(),
        'selected_sort': selected_sort,
        'themes': themes
    }
    return render(request, 'home.html', context)

class TermsAndConditionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'terms_and_condition.html')