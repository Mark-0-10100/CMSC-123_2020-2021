from django.db import models


# The code here creates the database for "Blogs"
class Blogs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)

    def get_absolute_url(self):
        return f"/blogs/{self.id}"  #Dynamic linking of the URL