from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator


class CityModel(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Название города')

    def __str__(self):
        return self.Name


class TypeModel(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Тема')

    def __str__(self):
        return self.Name


class MarkModel(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Ник')
    UserId = models.CharField(max_length=20, verbose_name='Идентификационный номер')
    Text = models.CharField(max_length=500, verbose_name='Комментарий')
    Score = models.IntegerField(verbose_name='Оценка')

    def __str__(self):
        return self.Name


class ProjectModel(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Название')
    Description = models.CharField(max_length=1000, verbose_name='Описание')
    # TeacherId = models.CharField(max_length=20)
    GithubLink = models.CharField(max_length=100)
    AccessLevel = models.IntegerField(verbose_name='Уровень доступа')
    AverageMark = models.IntegerField(default=0, verbose_name='Средняя оценка')
    ShowMainPage = models.BooleanField(default=False, verbose_name='На главной странице')
    ProjectImage = models.ImageField(upload_to='logos/', null=True,
                                     height_field=None, width_field=None, max_length=100,
                                     verbose_name='Изображение')

    City = models.ForeignKey(CityModel, verbose_name='Город', on_delete=models.CASCADE)
    Marks = models.ManyToManyField(MarkModel, verbose_name='Пользовательские оценки')
    Type = models.ManyToManyField(TypeModel, verbose_name='Теги')

    @property
    def photo_url(self):
        if self.ProjectImage and hasattr(self.ProjectImage, 'url'):
            return self.ProjectImage.url

    def __str__(self):
        return self.Name


# расширенный юзер с добавлением уровня доступа
class Person(AbstractUser):
    access_level = models.PositiveSmallIntegerField(default=1, verbose_name='Уровень доступа',
                                                    validators=[MaxValueValidator(5)])