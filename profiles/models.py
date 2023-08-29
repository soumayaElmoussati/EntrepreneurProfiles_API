from django.db import models

# Create your models here.


class EntrepreneurProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sector = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name