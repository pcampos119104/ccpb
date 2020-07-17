from django.db import models


class Member(models.Model):
    name = models.CharField('nome', max_length=50)
    address = models.CharField('endereço', max_length=200)

    def __str__(self):
        return self.name


class Phone(models.Model):
    number = models.CharField('numero', max_length=15)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.number
