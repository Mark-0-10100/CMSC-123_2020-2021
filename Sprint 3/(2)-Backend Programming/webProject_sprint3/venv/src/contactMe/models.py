from django.db import models

# The code here is for the database for "Contact Me"
class ContactMe (models.Model):
    name = models.CharField(max_length=120)
    email = models.TextField(blank=True, null=True)
    message = models.TextField(max_length=120)
