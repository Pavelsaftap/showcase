from django.db import models


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
