# Generated by Django 3.2.7 on 2021-09-23 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0003_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]