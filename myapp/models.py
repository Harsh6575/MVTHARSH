from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10, default='')
    email = models.EmailField()
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.name