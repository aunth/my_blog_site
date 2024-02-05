# core_app/admin.py
from django.contrib import admin
from post_app.models import Post

admin.site.register(Post)
