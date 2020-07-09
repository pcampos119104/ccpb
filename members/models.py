from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Phone(models.Model):
    number = models.CharField(max_length=15)
    # todo validate this line
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.number
