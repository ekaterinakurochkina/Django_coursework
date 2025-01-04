from django.db import models


class MailingRecipient(models.Model):           # Получатель рассылки
    email = models.EmailField(unique=True, verbose_name='Email')                    # Email
    name = models.CharField(max_length=150, verbose_name='ФИО', blank=True)           # ФИО
    comment = models.TextField(verbose_name='Комментарий', blank=True)               # комментарий

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Получатель рассылки'
        verbose_name_plural = 'Получатели рассылки'
        ordering = ['email']


class Message(models.Model):          #   Сообщение
    subject = models.CharField(max_length=300, verbose_name='Тема письма')           # тема письма
    message = models.TextField(verbose_name='Тело письма', blank=True)           # тело письма

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['subject']

class Sending(models.Model):           # Рассылка
    first_sending = models.DateTimeField(auto_now_add=True)              # Дата и время первой отправки
    end_sending = models.DateTimeField(auto_created=True, null=True, blank=True)               # Дата и время окончания отправки
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('launched', 'Запущена'),
        ('completed', 'Завершена'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')           # статус
    message = models.ForeignKey(Message, on_delete=models.SET_NULL)           # Сообщение (внешн.ключ на модель Сообщение)
    recipient = models.ManyToManyField(MailingRecipient)                      # Получатели (связь с моделью Получатель)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status']


class MailingAttempt(models.Model):           # Попытка рассылки
    date_attempt = models.DateTimeField(auto_now_add=True)              # Дата и время попытки
    STATUS_CHOICES = [
        ('successfully', 'Успешно'),
        ('unsuccessful', 'Неуспешно'),
    ]
    status_attempt = models.CharField(max_length=15, choices=STATUS_CHOICES, default='unsuccessful')      # Статус: успешно/неуспешно
    answer = models.TextField(blank=True, null=True)                                       # ответ почтового сервера
    sending = models.ForeignKey(Sending, on_delete=models.SET_NULL)               # рассылка (внешн.ключ на модель Рассылка)

    def __str__(self):
        return self.status_attempt

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
        ordering = ['status_attempt']


# class Category(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Наименование')
#     description = models.TextField(max_length=150, verbose_name='Описание', blank=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#         ordering = ['name']
#
# class Product(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Наименование')
#     description = models.TextField(max_length=150, verbose_name='Описание', blank=True)
#     image = models.ImageField(upload_to='images/', verbose_name='Изображение', null=True, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
#     price = models.IntegerField(verbose_name='Цена за покупку', null=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения', null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = 'Продукты'
#         ordering = ['name']