# Generated by Django 4.0.3 on 2022-04-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motionApp', '0005_remove_order_url_project_order_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='upload',
        ),
        migrations.AddField(
            model_name='order',
            name='url_project',
            field=models.URLField(blank=True, null=True, verbose_name='Укажите url путь'),
        ),
    ]
