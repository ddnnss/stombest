from django.db import models
from customuser.models import User



class Month(models.Model):
    name = models.CharField('Месяц', max_length=255, blank=False, null=True)
    def __str__(self):
        return 'Месяц : %s ' % self.name

    class Meta:
        verbose_name = "Месяц"
        verbose_name_plural = "Месяцы"

class Day(models.Model):
    name = models.CharField('День', max_length=255, blank=False, null=True)
    def __str__(self):
        return 'День : %s ' % self.name

    class Meta:
        verbose_name = "День"
        verbose_name_plural = "Дни"

class Time(models.Model):
    name = models.CharField('Время', max_length=255, blank=False, null=True)
    def __str__(self):
        return 'Время : %s ' % self.name

    class Meta:
        verbose_name = "Время"
        verbose_name_plural = "Время"


class ServiceCat(models.Model):
    name = models.CharField('Категория услуг', max_length=255,blank=False, null=True)
    ico = models.ImageField("Иконка для меню", blank=False, null=True)
    image = models.ImageField("Картинка в описании", blank=False, null=True)

    def __str__(self):
        return 'Категория : %s ' % self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Service(models.Model):
    name = models.CharField('Название услуги', max_length=255, blank=False, null=True)
    category = models.ManyToManyField(ServiceCat, blank=False, null=True, verbose_name='Категория услуг')
    description = models.TextField('Описание услуги', default='')

    def __str__(self):
        return 'Услуга : %s ' % self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class SubService(models.Model):
    name = models.CharField('Название разновидности услуги', max_length=255, blank=False, null=True)
    category = models.ForeignKey(Service, blank=False, on_delete=models.CASCADE, null=True, verbose_name='Для услуги')
    price = models.IntegerField('Цена', default=0)

    def __str__(self):
        return 'Услуга : %s ' % self.name

    class Meta:
        verbose_name = "Разновидность услуги"
        verbose_name_plural = "Разновидности услуг"

class Doctor(models.Model):
    name = models.CharField('ФИО Доктора', max_length=255,blank=False, null=True)
    cabinet = models.CharField('Кабинет', max_length=255, blank=False, null=True)
    specialization = models.CharField('Специализация', max_length=255, blank=False, null=True)
    image = models.ImageField("Картинка", blank=False, null=True)
    info = models.CharField('Инфо', max_length=255, blank=False, null=True)
    services = models.ManyToManyField(Service,blank=True,null=True,verbose_name='Предоставляет услуги')

    def __str__(self):
        return 'Врач : %s ' % self.name

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

class Apply(models.Model):
    doc = models.ForeignKey(Doctor,blank=True,null=True, on_delete=models.CASCADE)
    client = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    service = models.ForeignKey(SubService, blank=False, null=True, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, blank=False, null=True, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, blank=False, null=True, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        try:
            if self.doc.name:
                return 'Запись к врачу {} от {} телефон {}'.format(self.doc.name, self.client.name,
                                                               self.client.phone)
            else:
                return 'Запись к врачу  от {} телефон {}'.format( self.client.name,
                                                               self.client.phone)
        except:
            return 'Запись к врачу от пользователя без имени'
    class Meta:
        verbose_name = "Запись к врачу"
        verbose_name_plural = "Записи к врачам"

class Message(models.Model):
    client = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    message = models.TextField('Вопрос', blank=False, null=True)
    answer = models.TextField('Ответ', blank=False, null=True)

    def __str__(self):
        return 'Сообщение от {} '.format(self.client.name)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Banner(models.Model):
    image = models.ImageField("Картинка", blank=False, null=True)
    service = models.ForeignKey(Service, blank=True, null=True, on_delete=models.CASCADE,
                                verbose_name='Ссылается на услугу')

    def __str__(self):
        return 'Баннер : %s ' % self.id

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
