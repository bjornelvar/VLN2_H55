# Generated by Django 4.0.4 on 2022-05-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('passwordhash', models.CharField(max_length=500)),
                ('bio', models.CharField(blank=True, max_length=255)),
                ('rating', models.FloatField()),
                ('online', models.BooleanField(default=False)),
                ('image', models.ImageField(default=None, upload_to='')),
            ],
        ),
    ]
