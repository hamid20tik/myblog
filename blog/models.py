from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='media/')



    def __str__(self):
        return self.title
