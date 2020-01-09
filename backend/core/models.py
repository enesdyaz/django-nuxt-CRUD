from django.db import models

# Create your models here.
class Memo(models.Model):
    name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name