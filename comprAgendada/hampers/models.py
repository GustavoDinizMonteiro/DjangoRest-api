from django.db import models


class Hamper(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name = u'Hamper'
        verbose_name_plural = u'Hampers'

    def __str__(self):
        return "Name: %s" % self.name
