# Generated by Django 4.0.4 on 2022-05-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profiles_image_profileimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='passwordhash',
        ),
        migrations.AddField(
            model_name='profiles',
            name='image',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='profile_pics/'),
        ),
        migrations.DeleteModel(
            name='ProfileImages',
        ),
    ]
