# Generated by Django 4.2.7 on 2023-11-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_order_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(blank=True, help_text='Entrez la date au format JJ/MM/AA', null=True, verbose_name='Début de votre activité'),
        ),
    ]
