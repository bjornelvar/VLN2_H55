# Generated by Django 3.2.13 on 2022-05-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_remove_items_image_itemimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='has_accepted_offer',
            field=models.BooleanField(default=False),
        ),
    ]
