from django.db import models
from customuser.models import User

class Banner(models.Model):
    image = models.ImageField("Картинко", blank=False, null=True)


class Month(models.Model):
    name = models.CharField('Месяц', max_length=255, blank=False, null=True)


class Day(models.Model):
    name = models.CharField('День', max_length=255, blank=False, null=True)


class Time(models.Model):
    name = models.CharField('Время', max_length=255, blank=False, null=True)


class ServiceCat(models.Model):
    name = models.CharField('Категория услуг', max_length=255,blank=False, null=True)
    ico = models.ImageField("Иконко", blank=False, null=True)
    image = models.ImageField("Картинко", blank=False, null=True)
    tab1 = models.CharField('TAB1 название', max_length=255, blank=False, null=True)
    tab1text = models.CharField('TAB1 текст', max_length=255, blank=False, null=True)
    tab2 = models.CharField('TAB2 название', max_length=255, blank=False, null=True)
    tab2text = models.CharField('TAB2 текст', max_length=255, blank=False, null=True)
    tab3 = models.CharField('TAB3 название', max_length=255, blank=False, null=True)
    tab3text = models.CharField('TAB3 текст', max_length=255, blank=False, null=True)
    isChild = models.BooleanField('Детская услуга', default=False)

class Service(models.Model):
    name = models.CharField('Название услуга', max_length=255, blank=False, null=True)
    category = models.ManyToManyField(ServiceCat, blank=False, null=True, verbose_name='Категория услуг')
    price = models.IntegerField('Цена', default=0)

class Doctor(models.Model):
    name = models.CharField('ФИО Доктора', max_length=255,blank=False, null=True)
    cabinet = models.CharField('Кабинет', max_length=255, blank=False, null=True)
    image = models.ImageField("Картинко", blank=False, null=True)
    info = models.CharField('Инфо', max_length=255, blank=False, null=True)
    services = models.ManyToManyField(Service,blank=True,null=True,verbose_name='Предоставляет услуги')

class Apply(models.Model):
    doc = models.ForeignKey(Doctor,blank=True,null=True, on_delete=models.CASCADE)
    client = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, blank=False, null=True, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, blank=False, null=True, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, blank=False, null=True, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, blank=False, null=True, on_delete=models.CASCADE)
