from django.db import models

# Create your models here.
class Tickets(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    priority = models.CharField(max_length=20)
    
    def _str_(self):
        return self.title



