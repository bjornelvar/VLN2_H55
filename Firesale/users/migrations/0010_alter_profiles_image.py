# Generated by Django 4.0.4 on 2022-05-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_profiles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='image',
            field=models.ImageField(default='images/blank-profile-picture.png', upload_to='images/'),
        ),
    ]
