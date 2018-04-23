from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    price = models.FloatField(null=False)

    class Meta:
        verbose_name = u'Product'
        verbose_name_plural = u'Products'


    def __str__(self):
        return "Name: %s, Price: %.2f" % (self.name, self.price)
