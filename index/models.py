from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=300, blank=False)
    image = models.ImageField(upload_to="slider",blank=False)

    def str(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to="about",blank=False)

    def str(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to="random",blank=False)

    def str(self):
        return self.title
    

class App(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to="app",blank=False)

    def str(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to="product",blank=False)

    def str(self):
        return self.title