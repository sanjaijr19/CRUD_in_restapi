from django.db import models

# Create your models here.
class UserModel(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    contact_no=models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    sname=models.CharField(max_length=20)
    roll_no=models.IntegerField()
    place=models.CharField(max_length=50)