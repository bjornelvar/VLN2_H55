# Generated by Django 4.0.4 on 2022-05-09 15:28

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_alter_items_listdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.1'))]),
        ),
    ]
