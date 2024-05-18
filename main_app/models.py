from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    species = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    size = models.FloatField()

    def __str__(self):
        return f"A {self.species} has appeared with a length of {self.size} in."
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})