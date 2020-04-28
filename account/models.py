
from django.db import models


class image(models.Model):
    images = models.ImageField(default='default.png', blank=True)


class category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    imgCat = models.ImageField(default='default.png', blank=True)
     
    def __str__(self):
        return self.title



class product(models.Model):
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=25)
    productName = models.TextField(null=True)
    img = models.ForeignKey(image, on_delete=models.CASCADE, default=None)
    cat = models.ForeignKey(category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.productName    
