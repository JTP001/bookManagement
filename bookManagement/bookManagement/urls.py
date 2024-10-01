from django.contrib import admin
from django.urls import path
from inventory.views import AddInventoryFormView, ListInventoryView, export_inventory
from django.views.generic import TemplateView, RedirectView

# Paths to the urls of each of the pages.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="home/"), name="index"),
    path('home/', TemplateView.as_view(template_name="index.html"), name="homepage"),
    path('inventory/', ListInventoryView.as_view(), name="inventory_list"),
    path('add/', AddInventoryFormView.as_view(), name="add_book"),
    path('export/csv/', export_inventory, name="export_inventory"),
]
