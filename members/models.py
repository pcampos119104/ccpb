from django.db import models


class Member(models.Model):
    MARITAL_CHOICES = (
            ('single','Solteiro(a)'),
            ('married','Casado(a)'),
            ('divorced','Divorciado(a)'),
            ('widower','Viúvo(a)'),
            ('separate', 'Separado(a)')
            )

    name_member = models.CharField('nome', max_length=50)
    name_mother= models.CharField('nome mãe', max_length=50)
    name_father = models.CharField('nome pai', max_length=50)
    natural_from = models.CharField('natural de', max_length=50)
    marital_status = models.CharField('estado civil', max_length=10,
            choices=MARITAL_CHOICES)
    doc_id = models.CharField('RG', max_length=10)
    birth_dt = models.DateField('data de nascimento')
    member_since_dt = models.DateField('membro desde')
    baptism_dt = models.DateField('data de batismo')
    address = models.CharField('endereço', max_length=200)
    valid = models.IntegerField('validade')

    minister = models.ForeignKey('Minister', 
            verbose_name='Pastor', 
            on_delete=models.SET_NULL, 
            blank=True,
            null=True,
            )

        
    class Meta:
        verbose_name = 'membro'
        verbose_name_plural = 'membros'

    def __str__(self):
        return self.name_member


class Phone(models.Model):
    number = models.CharField('numero', max_length=15)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

        
    class Meta:
        verbose_name = 'telefone'
        verbose_name_plural = 'telefones'


    def __str__(self):
        return self.number


class Minister(models.Model):
    name = models.CharField('nome', max_length=50)

        
    class Meta:
        verbose_name = 'pastor'
        verbose_name_plural = 'pastores'

     
    def __str__(self):
        return self.name
