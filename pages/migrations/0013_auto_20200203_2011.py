# Generated by Django 2.2.7 on 2020-02-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20200203_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='isRead',
            field=models.BooleanField(default=False, verbose_name='Прочитано ?'),
        ),
    ]