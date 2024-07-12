from django.db import models

class Publications(models.Model):
   title = models.CharField(max_length=200)
   short_description = models.TextField()
   description = models.TextField()
   image = models.ImageField()
   create_date = models.DateTimeField()


class Coffees(models.Model):
   name = models.CharField(max_length=150)
   price = models.FloatField()
   img = models.ImageField()
   consist = models.TextField()
   IsIce = models.BooleanField(null=True)


class Discord(models.Model):
   name = models.CharField(max_length=50)
   contein = models.TextField()
   img = models.ImageField()