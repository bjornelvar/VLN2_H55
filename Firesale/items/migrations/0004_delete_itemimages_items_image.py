# Generated by Django 4.0.4 on 2022-05-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_itemimages_remove_items_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemImages',
        ),
        migrations.AddField(
            model_name='items',
            name='image',
            field=models.ImageField(default='no-image-default.png', upload_to='item_pics/'),
        ),
    ]
