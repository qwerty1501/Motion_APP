from django.db import models


class FeedbackLink(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=30,
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=100,
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=30,
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        blank=True,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'