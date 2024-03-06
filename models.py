from django.db import models
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=10)
    picture=models.ImageField(upload_to='schoolimg',null=True)

class Identity(models.Model):
    idno=models.IntegerField()
    name=models.CharField(max_length=100)

class Person(models.Model):
    fullname=models.CharField(max_length=30)
    identity=models.OneToOneField(Identity,on_delete=models.CASCADE)

class Compensation(models.Model):
    name = models.CharField(max_length=255)

class Firm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    compensations = models.ManyToManyField(Compensation)

class Enroll(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    # student=models.ForeignKey(Student,on_delete=models.CASCADE)
    # course=models.CharField(max_length=30)
    # fees=models.IntegerField(max_length=30)
    # duration=models.CharField(max_length=50)






