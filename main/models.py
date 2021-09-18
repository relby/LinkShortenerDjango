from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Links(models.Model):
    url = URLField(max_length=2500)
    shortened_url = URLField(max_length=100)

    def __str__(self):
        return str(self.url)