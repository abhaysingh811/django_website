from django.db import models
#register your model here
class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=15)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
