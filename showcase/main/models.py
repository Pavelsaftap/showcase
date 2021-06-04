from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator


class CityModel(models.Model):
    Name = models.CharField(max_length=50)


class TypeModel(models.Model):
    Name = models.CharField(max_length=50)


class MarkModel(models.Model):
    Name = models.CharField(max_length=50)
    UserId = models.CharField(max_length=20)
    Text = models.CharField(max_length=500)
    Score = models.IntegerField()


class ProjectModel(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=1000)
    # TeacherId = models.CharField(max_length=20)
    GithubLink = models.CharField(max_length=100)
    AccessLevel = models.IntegerField()
    AverageMark = models.IntegerField(default=0)
    ShowMainPage = models.BooleanField(default=False)

    City = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    Marks = models.ManyToManyField(MarkModel)
    Type = models.ManyToManyField(TypeModel)


# расширенный юзер с добавлением уровня доступа
class Person(AbstractUser):
    access_level = models.PositiveSmallIntegerField(default=1, verbose_name='Уровень доступа',
                                                    validators=[MaxValueValidator(5)])



