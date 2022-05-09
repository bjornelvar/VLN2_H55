# Generated by Django 4.0.4 on 2022-05-09 16:24

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0004_alter_bids_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bids',
            name='bidamount',
            field=models.DecimalField(decimal_places=1, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.1'))]),
        ),
        migrations.DeleteModel(
            name='Accepts',
        ),
    ]