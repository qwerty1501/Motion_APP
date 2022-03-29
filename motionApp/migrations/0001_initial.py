# Generated by Django 4.0.3 on 2022-03-28 12:04

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/person', verbose_name='Фотография')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('url_instagram', models.URLField(blank=True, null=True, verbose_name='Укажите сылку на ваш instagram (*Не обязательно)')),
                ('url_facebook', models.URLField(blank=True, null=True, verbose_name='Укажите сылку на ваш facebook (*Не обязательно)')),
                ('url_mail', models.URLField(blank=True, null=True, verbose_name='Укажите сылку на ваш mail (*Не обязательно)')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Введите описание')),
            ],
            options={
                'verbose_name': 'Вакансию',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/poduct', verbose_name='Фотография')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('url_project', models.URLField(blank=True, null=True, verbose_name='Укажите url путь')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]