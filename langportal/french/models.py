from django.db import models




class dictionary(models.Model):
    english = models.CharField(max_length=100)
    type = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    french = models.CharField(max_length=100)
    
    



