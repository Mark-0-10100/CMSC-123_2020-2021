from django.db import models

# The code here creates the database for "Project Portfolio"
class Portfolio_softProj(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=800)

class Portfolio_artProj(models.Model):
    title = models.CharField(max_length=50)

class Portfolio_researchProj(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=800)   

class Portfolio_progressProj(models.Model):
    title = models.CharField(max_length=50) 
    description = models.TextField(max_length=800)

class Portfolio_futureProj(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=800)