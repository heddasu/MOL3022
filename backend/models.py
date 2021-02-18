from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Pfm(models.Model):
    adenin = ArrayField(models.IntegerField(), null=True)
    thymine = ArrayField(models.IntegerField(), null=True)
    cytosine = ArrayField(models.IntegerField(), null=True)
    guanine = ArrayField(models.IntegerField(), null=True)

class Matrix(models.Model):
    matrix_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=20, null=True)
    pfm = models.ForeignKey(Pfm, on_delete=models.CASCADE, null=True)