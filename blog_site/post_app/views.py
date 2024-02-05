from django.views import generic
from django.shortcuts import render, redirect
from post_app.models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect



class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'home.html'
	
	def render_to_response(self, context, **response_kwargs):
		print(context)  # Add this line to print context
		return super().render_to_response(context, **response_kwargs)


@login_required
def create_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			# Create a new post object but don't save it yet
			new_post = form.save(commit=False)
			new_post.author = request.user  # Set the author to the currently logged-in user
			new_post.save()  # Now save the post with the author information
			return redirect('profile')  # Redirect to the home page or post list page
	else:
		form = PostForm()


	return render(request, 'create_post.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the user has already liked the post
    liked_before = request.session.get(f'post_{pk}_liked', False)

    if request.method == 'POST' and not liked_before:
        # Check if the like button is clicked
        if 'like_button' in request.POST:
            post.likes += 1
            post.save()

            # Set a session variable to indicate that the user has liked the post
            request.session[f'post_{pk}_liked'] = True

            return HttpResponseRedirect(request.path)

    return render(request, 'post_detail.html', {'post': post, 'liked_before': liked_before})


	