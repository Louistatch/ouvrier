# Generated by Django 4.2.7 on 2023-11-03 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_manpowerneeds_delete_prefecture_delete_region'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ManpowerNeeds',
            new_name='order',
        ),
    ]
