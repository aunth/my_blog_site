import os
import sys
from django.core.management import execute_from_command_line
from django.utils.text import slugify

# Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

# Configure Django settings using manage.py
execute_from_command_line(sys.argv)

# Now you can import Django models
from post_app.models import Post
from django.contrib.auth.models import User

def create_test_posts():
    # Create a test user with a unique username
    user = User.objects.create_user('teslfajsldjflasjdl;f', 'testuser1@example.com', 'passwordlfkasldkfjal;sdfk')

    # Create a few test posts
    posts_data = [
        {'title': 'Test Post 1', 'content': 'This is the content of Test Post 1.'},
        {'title': 'Test Post 2', 'content': 'This is the content of Test Post 2.'},
        {'title': 'Test Post 3', 'content': 'This is the content of Test Post 3.'},
    ]

    for post_data in posts_data:
        # Generate a unique slug
        base_slug = slugify(post_data['title'])
        slug = base_slug
        counter = 1
        while Post.objects.filter(slug=slug).exists():
            slug = f'{base_slug}-{counter}'
            counter += 1

        # Generate a unique title
        base_title = post_data['title']
        title = base_title
        counter = 1
        while Post.objects.filter(title=title).exists():
            title = f'{base_title} {counter}'
            counter += 1

        Post.objects.create(
            title=title,
            content=post_data['content'],
            author=user,
            slug=slug
        )

if __name__ == '__main__':
    create_test_posts()
    print('Test posts created successfully!')
