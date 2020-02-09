# Generated by Django 2.2.7 on 2020-02-03 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20200116_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Адрес')),
                ('phone1', models.CharField(max_length=255, null=True, verbose_name='Телефон1')),
                ('phone2', models.CharField(max_length=255, null=True, verbose_name='Телефон2')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='Email')),
                ('time', models.CharField(max_length=255, null=True, verbose_name='Время работы')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='isRead',
            field=models.BooleanField(default=True, verbose_name='Прочитано ?'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Day'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='month',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Month'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Time'),
        ),
        migrations.AlterField(
            model_name='servicecat',
            name='ico',
            field=models.ImageField(null=True, upload_to='', verbose_name='Иконка для меню 60x60'),
        ),
        migrations.AlterField(
            model_name='subservice',
            name='price',
            field=models.CharField(max_length=10, null=True, verbose_name='Цена'),
        ),
    ]