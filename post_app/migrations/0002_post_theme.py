# Generated by Django 5.0.1 on 2024-01-25 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='theme',
            field=models.CharField(blank=True, choices=[('technology', 'Technology'), ('science', 'Science'), ('travel', 'Travel')], max_length=50),
        ),
    ]