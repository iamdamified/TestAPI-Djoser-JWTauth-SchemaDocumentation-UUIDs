from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    content = models.TextField()

    def __str__(self):
        return self.title
