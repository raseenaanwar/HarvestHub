# Generated by Django 5.1.2 on 2024-10-30 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_fooditem_type_fooditem_food_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='category',
        ),
    ]
