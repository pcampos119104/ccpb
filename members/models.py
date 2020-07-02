from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)


class Phone(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    number = models.CharField(max_length=15)
