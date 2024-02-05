# print_posts.py

import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
django.setup()

# Import the Post model
from post_app.models import Post

def print_all_posts():
    # Retrieve all posts from the database
    all_posts = Post.objects.all()

    # Print information about each post
    for post in all_posts:
        print(f"Post ID: {post.id}")
        print(f"Title: {post.title}")
        print(f"Content: {post.content}")
        print("\n")

if __name__ == "__main__":
    print_all_posts()
