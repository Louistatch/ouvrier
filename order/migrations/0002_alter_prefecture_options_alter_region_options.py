# Generated by Django 4.2.7 on 2023-11-02 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prefecture',
            options={'permissions': [('can_delete_prefecture', 'Peut supprimer une préfecture')]},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'permissions': [('can_delete_region', 'Peut supprimer une région')]},
        ),
    ]