from django.contrib import admin

from .models import order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('farm_name', 'region', 'production_type', 'start_date')  # Les champs que vous souhaitez afficher dans la liste
    list_filter = ('region', 'production_type', 'start_date')  # Les champs pour lesquels vous souhaitez des filtres
    search_fields = ('farm_name', 'region', 'production_type')  # Les champs que vous souhaitez rechercher
# Enregistrez le modèle dans l'administration

admin.site.register(order, OrderAdmin)


