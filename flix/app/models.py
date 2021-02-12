from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255) 
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    
    
class Serie(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255) 
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name    
