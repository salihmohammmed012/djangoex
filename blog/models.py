from django.db import models
class Post(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    phone_no = models.PositiveIntegerField()
    resume = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name
# Create your models here.
