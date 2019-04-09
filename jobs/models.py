from django.db import models

class job(models.Model):
    image = models.ImageField(upload_to='image/')
    summery = models.CharField(max_length=200)