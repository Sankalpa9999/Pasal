# Generated by Django 5.0.3 on 2024-04-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]