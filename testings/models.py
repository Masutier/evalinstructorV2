from django.db import models


class Testings(models.Model):
    ficha = models.CharField(max_length=9)
    aprendiz = models.CharField(max_length=10)
    instructor = models.CharField(max_length=10)
    p01 = models.CharField(max_length=1)
    p02 = models.CharField(max_length=1, null=True)
    p03 = models.CharField(max_length=1, null=True)
    p04 = models.CharField(max_length=1, null=True)
    p05 = models.CharField(max_length=1)
    p06 = models.CharField(max_length=1, null=True)
    p07 = models.CharField(max_length=1, null=True)
    p08 = models.CharField(max_length=1, null=True)
    p09 = models.CharField(max_length=1, null=True)
    p10 = models.CharField(max_length=1, null=True)
    p11 = models.CharField(max_length=1, null=True)
    p12 = models.CharField(max_length=1)

    def __str__(self):
        return self.ficha

