from django.db import models

class Student(models.Model):
    uusername = models.CharField(max_length=200)
    uparentsname = models.CharField(max_length=200)
    uage = models.CharField(max_length=100)
    uemail = models.EmailField()
    uaddress = models.CharField(max_length=255)
    upincode = models.CharField(max_length=10)
    ucontactnumber = models.CharField(max_length=10)
    udate = models.CharField(max_length=10)  
    unationality = models.CharField(max_length=50)

    class Meta:
        db_table = "student"


