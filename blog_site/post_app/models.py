from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

POST_THEME = ['']

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    theme = models.CharField(max_length=50, choices=[
        ('technology', 'Technology'),
        ('science', 'Science'),
        ('travel', 'Travel'),
        ('finance', 'Finance'),
        ('relationships', 'Relationships'),
        ('beauty', 'Beauty'),
        ('fashion', 'Fashion'),
        ('education', 'Education'),
        ('healthy', 'Healthy')
    ], blank=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
