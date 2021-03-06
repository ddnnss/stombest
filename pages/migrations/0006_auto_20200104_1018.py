# Generated by Django 2.2.7 on 2020-01-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20191218_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecat',
            name='isChild',
        ),
        migrations.RemoveField(
            model_name='servicecat',
            name='tab1',
        ),
        migrations.RemoveField(
            model_name='servicecat',
            name='tab1text',
        ),
        migrations.RemoveField(
            model_name='servicecat',
            name='tab2',
        ),
        migrations.RemoveField(
            model_name='servicecat',
            name='tab2text',
        ),
        migrations.RemoveField(
            model_name='servicecat',
            name='tab3',
        ),
        migrations.RemoveField(
            model_name='servicecat',
            name='tab3text',
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(default='', verbose_name='Описание услуги'),
        ),
        migrations.AlterField(
            model_name='servicecat',
            name='ico',
            field=models.ImageField(null=True, upload_to='', verbose_name='Иконка для меню'),
        ),
        migrations.AlterField(
            model_name='servicecat',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Картинка в описании'),
        ),
    ]
