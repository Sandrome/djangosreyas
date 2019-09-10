from django.db import models

class Employee(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')]
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    age = models.IntegerField()
    empid = models.IntegerField(null=False)
    submission_date = models.DateTimeField()
    interests = models.ManyToManyField('Interests', blank=True)

class Interests(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name