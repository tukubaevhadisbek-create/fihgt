from django.db import models

class Trenery(models.Model):
    image = models.ImageField(upload_to='trainers/',verbose_name='Тренеры')
    name = models.CharField(max_length=20,verbose_name='Имя')
    sport = models.CharField(max_length=20,verbose_name='Спорт')
    experiense = models.IntegerField(verbose_name='Опыт')
    description= models.TextField(max_length=250,verbose_name="Описание")

    class Meta:
        verbose_name='Тренер'
        verbose_name_plural = "Тренеры"
    def __str__(self):
        return self.name
class Schedule(models.Model):
    day = models.CharField(max_length=20,verbose_name='Дни')
    time = models.TimeField(verbose_name='Время')
    group=models.CharField(max_length=20,verbose_name='Группа')
    class Meta:
            verbose_name='Расписание'
            verbose_name_plural = "Расписание"
    def __str__(self):
        return self.day
class Price(models.Model):
    type=models.CharField(max_length=20,verbose_name='вид тренировок')
    price=models.IntegerField(verbose_name='Цена на тренировку')
    bonus1=models.CharField(max_length=50,verbose_name='Что входит в цену')
    bonus2=models.CharField(max_length=50,verbose_name='Что входит в цену')
    bonus3=models.CharField(max_length=50,verbose_name='Что входит в цену')
    class Meta:
        verbose_name='Цена'
        verbose_name_plural = "Цены"
    def __str__(self):
        return self.type
class Contact(models.Model):
    phone = models.CharField( max_length=20,verbose_name='Номер телефона')
    telegram = models.CharField(max_length=30,verbose_name='Телеграм')
    map = models.CharField(max_length=40,verbose_name='Местоположение')
    email = models.EmailField(verbose_name='Email')
    class Meta:
        verbose_name='Контакт'
        verbose_name_plural = "Контакты"
    def __str__(self):
        return self.telegram
class Training(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    naprav = models.CharField(max_length=20, verbose_name='Направление')
    description = models.TextField(
        max_length=250,
        verbose_name='Описание',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрации"

    def __str__(self):
        return self.name
    
class Direction(models.Model):
    name = models.CharField(max_length=100,verbose_name='Направление')

    class Meta:
        verbose_name="Направление"
        verbose_name_plural = "Направление"

    def __str__(self):
        return self.name