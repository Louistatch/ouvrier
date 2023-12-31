# Generated by Django 4.2.7 on 2023-11-04 23:49

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_area_unit_alter_order_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='required_workers',
            field=models.IntegerField(verbose_name='Nombre de métayer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateField(help_text='Entrez la date au format JJ/MM/AA', verbose_name='Début de votre activité'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tasks_to_perform',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sarclage', 'Sarclage'), ('amenagement_site', 'Aménagement du site'), ('prise_en_charge_ferme', 'Prise en charge de la ferme'), ('dessouchage', 'Dessouchage'), ('semis', 'Semis'), ('recolte', 'Récolte'), ('herbicide', 'Herbicide'), ('epandage_engrais', 'Épandage engrais'), ('surveillant', 'Surveillant'), ('agronome_serieux', 'Agronome sérieux')], max_length=50, verbose_name='Tâches à effectuer'),
        ),
    ]
