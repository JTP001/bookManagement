from django.core.exceptions import ValidationError
from django import forms
from .models import Inventory
import re

# This is a form class that makes it simple to create the book adding form 
# based on the Inventory model.
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['entryID', 'title', 'author', 'genre', 'pubDate', 'isbn']
        widgets = {
            'pubDate': forms.DateInput(attrs={'type':'date'}),
        }

    # This init is used just to override the default Django template look 
    # of the form to instead use Bootstrap.
    def __init__(self, *args, **kwargs):
        super(InventoryForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
        })

    # The clean method is used for custom validation.
    def clean(self):
        cleaned_data = super(InventoryForm, self).clean()

        # Checks if there is another entry with the same ID
        entryID = cleaned_data.get("entryID")
        dupe = Inventory.objects.all().filter(entryID=entryID)
        if dupe.exists():
            self.add_error('entryID', "A book with this ID already exists in the database.")
        
        # Checks if the isbn number matches the regex of a correct isbn
        isbn = cleaned_data.get("isbn")
        if isbn is not None and not re.match(r"(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)", isbn):
            self.add_error('isbn', "Invalid ISBN number.")
        
        return super().clean()