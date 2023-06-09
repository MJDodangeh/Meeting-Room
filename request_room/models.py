from django.db import models
from account.models import User

class RequestRoom(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,null=True)
    number = models.IntegerField()
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    duration = models.TimeField(null=True)
    Type_Choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    ]
    type = models.IntegerField(choices=Type_Choices,default=2)

class RequestWarning(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,null=True)
    number = models.IntegerField()
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    duration = models.TimeField(null=True)
    Type_Choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    ]
    type = models.IntegerField(choices=Type_Choices,default=2)