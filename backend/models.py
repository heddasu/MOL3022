from django.db import models
#from django.contrib.postgres.fields import ArrayField, 



# Create your models here.
class Pfm(models.Model):
    adenin = models.JSONField(models.FloatField(), null=True)
    thymine = models.JSONField(models.FloatField(), null=True)
    cytosine = models.JSONField(models.FloatField(), null=True)
    guanine = models.JSONField(models.FloatField(), null=True)

class Matrix(models.Model):
    matrix_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=20, null=True)
    pfm = models.ForeignKey(Pfm, on_delete=models.CASCADE, null=True)