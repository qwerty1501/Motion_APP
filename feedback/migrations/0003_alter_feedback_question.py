# Generated by Django 4.0.3 on 2022-03-30 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='question',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
    ]
