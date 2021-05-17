from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(null=False)
    phone = models.FloatField(null=False)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.first_name

# Create your models here.
