# Generated by Django 4.0.4 on 2022-05-12 14:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0016_rename_reviewer_review_rated_by_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Ratings',
        ),
    ]
