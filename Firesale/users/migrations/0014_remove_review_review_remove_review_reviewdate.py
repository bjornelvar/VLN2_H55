# Generated by Django 4.0.4 on 2022-05-12 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewdate',
        ),
    ]
