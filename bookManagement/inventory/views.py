from django.views.generic import CreateView, ListView
from django.urls import reverse
from .models import Inventory
from .InventoryForm import InventoryForm
import django_filters
from django.http import HttpResponse
import csv

# This is the view for the page where you add a book to the inventory.
# It uses django generic view CreateView to cimplify things.
class AddInventoryFormView(CreateView):
    form_class = InventoryForm
    template_name = 'add.html'

    # When you have added a book, you are sent to the list page to see it.
    def get_success_url(self):
        url = reverse("inventory_list")
        return url

# This view is a combination of the django generic ListView for listing 
# model objects, as well as the django filter plugin and its classes.
class FilteredListView(ListView):
    filterset_class = None

    # This gets the filter data based on the form inputs queryset.
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()
    
    # This overrides the data on the Django template. It gives the context
    # of the filter data to the template while also changing the look 
    # of the fields to use Bootstrap.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for field in iter(self.filterset.form.fields):
            # This is what overrides the visuals to use Bootstrap for
            # each field.
            self.filterset.form.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
            # This is used to make it clear what format the pubDate 
            # filter input needs to be in.
            if field == 'pubDate':
                self.filterset.form.fields[field].widget.attrs.update({
                'placeholder': 'yyyy-mm-dd',
                })
        context['filterset'] = self.filterset
        return context

# This is a view required by the Django filter plugin to define what
# fields should be in the filter form.
class InventoryFilterset(django_filters.FilterSet):
    class Meta:
        model = Inventory
        fields = ['title', 'author', 'genre', 'pubDate']

    # This init just makes sure all filter data has a default value
    # of '' so that there are no None values that break things.
    def __init__(self, data, *args, **kwargs):
        data = data.copy()
        data.setdefault('title', '')
        data.setdefault('author', '')
        data.setdefault('genre', '')
        data.setdefault('pubDate', '')
        super().__init__(data, *args, **kwargs)

# This is the view for the page where you see the inventory list.
# It uses the FilteredListView and just says what model is being used,
# what filterset class is being used, and which template is being used.
class ListInventoryView(FilteredListView):
    model = Inventory
    template_name = "list.html"
    filterset_class = InventoryFilterset

# This is a view for just the export button on the main page. 
def export_inventory(request):
    # This creates an HTTP response with the csv content type and tells
    # the page to download it as an attachment file called inventory.csv.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inventory.csv"'

    # This creates a csv writer to be able to write to a csv file.
    writer = csv.writer(response)
    
    # This writes each of the column headers
    writer.writerow(['entryID', 'title', 'author', 'genre', 'pubDate', 'isbn'])
    
    # This writes each of the rows using the database data.
    for book in Inventory.objects.all():
        writer.writerow([book.entryID, book.title, book.author, book.genre, book.pubDate, book.isbn])
    
    return response