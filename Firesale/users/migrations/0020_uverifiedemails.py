# Generated by Django 4.0.4 on 2022-05-13 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0019_merge_20220513_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='UverifiedEmails',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
