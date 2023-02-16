from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    """ Now it is not using, but can be usefull in case of custom user model needs """
    pass


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """ String for representing the Model object. """
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Categories"


class Gift(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        """ String for representing the Model object. """
        return f'{self.name}'

