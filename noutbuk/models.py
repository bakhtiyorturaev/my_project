from django.db import models

# Create your models here.


class Noutbuk(models.Model):
    name_n = models.CharField(max_length=20)
    make_n = models.CharField(max_length=20)
    year_n = models.IntegerField()
    color_n = models.CharField(max_length=15)
    price_n = models.DecimalField(max_digits=11, decimal_places=2)
    image_n = models.ImageField(upload_to='media')

    def __str__(self):
        return f"{self.name_n} | {self.year_n} | {self.color_n}"
