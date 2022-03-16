from django.db import models

# Create your models here.

class signupMaster(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField()


class notesMaster(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    selectfile=models.FileField(upload_to="NotesFolder")
    comments=models.TextField()