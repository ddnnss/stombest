from django.db import models
from customuser.models import User

class Banner(models.Model):
    image = models.ImageField("Картинко", blank=False, null=True)



class Doctor(models.Model):
    name = models.CharField('ФИО Доктора', max_length=255,blank=False, null=True)
    cabinet = models.CharField('Кабинет', max_length=255, blank=False, null=True)


class Service(models.Model):
    name = models.CharField('Услуга', max_length=255,blank=False, null=True)
    ico = models.ImageField("Иконко", blank=False, null=True)
    image = models.ImageField("Картинко", blank=False, null=True)
    tab1 = models.CharField('TAB1 название', max_length=255, blank=False, null=True)
    tab1text = models.CharField('TAB1 текст', max_length=255, blank=False, null=True)
    tab2 = models.CharField('TAB2 название', max_length=255, blank=False, null=True)
    tab2text = models.CharField('TAB2 текст', max_length=255, blank=False, null=True)
    tab3 = models.CharField('TAB3 название', max_length=255, blank=False, null=True)
    tab3text = models.CharField('TAB3 текст', max_length=255, blank=False, null=True)


class Apply(models.Model):
    doc = models.ForeignKey(Doctor,blank=False,null=True, on_delete=models.CASCADE)
    client = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
