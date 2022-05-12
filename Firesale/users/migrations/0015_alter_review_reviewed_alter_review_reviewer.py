# Generated by Django 4.0.4 on 2022-05-12 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0014_remove_review_review_remove_review_reviewdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]