# Generated by Django 4.0.4 on 2022-05-06 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0010_alter_profiles_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='id',
        ),
        migrations.AlterField(
            model_name='profiles',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
