from django.apps import AppConfig

# Added the Inventory app here so Django knows where to look for app files.
class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'
