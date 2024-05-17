from django.db import models
import uuid

# Create your models here.
class Finch(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    species = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    size = models.IntegerField()

    def __str__(self):
        return f"A {self.species} has appeared with a length of {self.size} in."
    