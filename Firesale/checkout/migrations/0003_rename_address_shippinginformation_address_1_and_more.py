# Generated by Django 4.0.4 on 2022-05-12 01:49

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_shippinginformation_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippinginformation',
            old_name='address',
            new_name='address_1',
        ),
        migrations.RemoveField(
            model_name='shippinginformation',
            name='state_province_region',
        ),
        migrations.AddField(
            model_name='shippinginformation',
            name='address_2',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='shippinginformation',
            name='first_name',
            field=models.CharField(default='Bob', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippinginformation',
            name='last_name',
            field=models.CharField(default='The builder', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shippinginformation',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
