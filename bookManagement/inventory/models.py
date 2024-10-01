from django.db import models
from django.core.exceptions import ValidationError

# Django models make it easy to do a database relation by abstracting
# away from the actual database script writing. It does all that for you,
# you just write the fields needed.
class Inventory(models.Model):

    entryID = models.IntegerField()
    title = models.CharField(max_length=100, default="", blank=False)
    author = models.CharField(max_length=50, default="", blank=False)
    genre = models.CharField(max_length=50, default="", blank=False)
    pubDate = models.DateField()
    isbn = models.CharField(max_length=17)

    # This clean method does validation on the model level for 
    # invalid inputs. Here that would only really be the entryID
    # being a positive integer, the rest is validated through the form.
    def clean(self):
        if self.entryID is None or self.entryID <= 0:
            raise ValidationError("Entry ID should be a positive integer.")

    def __str__(self):
        return self.title