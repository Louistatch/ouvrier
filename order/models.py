from django.db import models
import gettext
from multiselectfield import MultiSelectField
from django.contrib.admin.widgets import AdminDateWidget
from django.conf import settings


_ = gettext.gettext


class order(models.Model):
    REGION_CHOICES = (
        ('Maritime', _('Maritime')),
        ('Plateaux', _('Plateaux')),
        ('Centrale', _('Centrale')),
        ('Kara', _('Kara')),
        ('Savanes', _('Savanes')),
        )
    AREA_UNIT_CHOICES = (
        ('m2', _('Mètre carré')),
        ('ha', _('Hectares')),
        ('lots', _('Lots (600m²)')),
        )
    
    farm_name = models.CharField(max_length=100, verbose_name=_('Nom de la ferme'))
    region = models.CharField(
        max_length=50,
        choices=REGION_CHOICES,
        verbose_name=_('Région')
        )    
    prefecture = models.CharField(max_length=100, verbose_name=_('Préfecture'))
    canton = models.CharField(max_length=100, verbose_name=_('Canton'))
    village = models.CharField(max_length=100, verbose_name=_('Village'))
    phone_number = models.CharField(max_length=20, verbose_name=_('Numéro de téléphone'))
    production_type = models.CharField(max_length=100, verbose_name=_('Type de production'))
    area= models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Superficie (Valeur)'),
        help_text=_('Entrez la valeur de la superficie')
        )
    area_unit = models.CharField(
        max_length=10,
        choices=AREA_UNIT_CHOICES,
        verbose_name=_('Unité de superficie')
        )    
    
    current_employees = models.IntegerField(verbose_name=_('Nombre d\'employés actuels'))
    start_date = models.DateField(
        blank=True, null=True,
        verbose_name=_('Début de votre activité'),
        help_text='Entrez la date au format JJ/MM/AA',
        )

    required_workers = models.IntegerField(verbose_name=_('Nombre de métayer'))
    
    TASK_CHOICES = (
    ('sarclage', 'Sarclage'),
    ('amenagement_site', 'Aménagement du site'),
    ('prise_en_charge_ferme', 'Prise en charge de la ferme'),
    ('dessouchage', 'Dessouchage'),
    ('semis', 'Semis'),
    ('recolte', 'Récolte'),
    ('herbicide', 'Herbicide'),
    ('epandage_engrais', 'Épandage engrais'),
    ('surveillant', 'Surveillant'),
    ('agronome_serieux', 'Agronome sérieux'),
)
    
    tasks_to_perform = MultiSelectField (
        choices=TASK_CHOICES,
        max_choices=10,  # Nombre maximal d'activités sélectionnables
        max_length=50,  # Longueur maximale du champ
        verbose_name=_('Tâches à effectuer')
)

    work_schedule = models.CharField(
        choices=(
            ('full_time', _('Temps plein')),
            ('part_time', _('Temps partiel')),
            ('shifts', _('Horaires variables (équipes)')),
        ),
        verbose_name=_('Conditions de travail'),
        max_length=10
    )

    def __str__(self):
        return self.farm_name

    class Meta:
        verbose_name = _('Besoins en main-d\'œuvre')
        verbose_name_plural = _('Besoins en main-d\'œuvre')
