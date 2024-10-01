from django.contrib import admin
from .models import Inventory

# Registered the Inventory model so it can be changed in the admin panel.
admin.site.register(Inventory)