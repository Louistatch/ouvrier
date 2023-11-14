from django.db import models



# marketlink/models.py

from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_market_available = models.BooleanField(default=False, verbose_name="Marché disponible")

    def __str__(self):
        return self.name



class Product(models.Model):
    UNIT_CHOICES = [
        ('Kg', 'Kilogramme'),
        ('Bol', 'Bol'),
        ('Ablodegbadja', 'Ablodégbadja'),
        ('Unite', 'Unité'),
        # Ajoutez d'autres choix au besoin
    ]

    SELLER_CHOICES = [
        ('A', 'Agrégateur'),
        ('P', 'Producteur'),
        ('I', 'Intermediaire'),
        # Ajoutez d'autres choix au besoin
    ]

    REGION_CHOICES = [
        ('Savane', 'Savane'),
        ('Kara', 'Kara'),
        ('Centrale', 'Centrale'),
        ('Plateaux', 'Plateaux'),
        ('Maritime', 'Maritime'),
        # Ajoutez d'autres choix au besoin
    ]
    AVAILABILITY_CHOICES = [
        ('yes', 'Oui'),
        ('no', 'Non'),
    ]

    seller_name = models.CharField(max_length=255, verbose_name="Nom du vendeur ou de la structure")
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Catégorie de produit")
    region = models.CharField(max_length=20, choices=REGION_CHOICES, verbose_name="Région")
    address = models.CharField(max_length=255, verbose_name="Adresse")
    status = models.CharField(max_length=1, choices=SELLER_CHOICES, verbose_name="Statut")
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, verbose_name="Unité")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Prix en FCFA")
    is_product_available = models.CharField(max_length=3, choices=AVAILABILITY_CHOICES, verbose_name="Produit disponible")
    quantity_available = models.PositiveIntegerField(null=True, blank=True, verbose_name="Quantité disponible")
    quantity_to_produce = models.PositiveIntegerField(null=True, blank=True, verbose_name="Quantité à produire")
    availability_date = models.DateField(null=True, blank=True, verbose_name="Date de disponibilité")
    phone_number = models.CharField(max_length=11, verbose_name="Numéro de téléphone")
    email = models.EmailField(default='votre@email.com')
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.seller_name} - {self.product_category}"
    
    def save(self, *args, **kwargs):
        if self.is_product_available == 'no':
            self.quantity_to_produce = None
            self.availability_date = None
        elif self.is_product_available == 'yes':
            self.quantity_available = None
        super(Product, self).save(*args, **kwargs)
