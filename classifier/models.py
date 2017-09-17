from django.db import models

# Create your models here.

class InterestArea(models.Model):
	interest = models.CharField(max_length=50)

class MCC(models.Model):
	companyName   = models.CharField(max_length=50)
	copmanyDomain = models.CharField(max_length=50)