from django.db import models


class CityModel(models.Model):
    # Id = models.CharField(max_length=20)
    Name = models.CharField(max_length=50)


class TypeModel(models.Model):
    # Id = models.CharField(max_length=20)
    Name = models.CharField(max_length=50)


class MarkModel(models.Model):
    # Id = models.CharField(max_length=20)
    Name = models.CharField(max_length=50)
    UserId = models.CharField(max_length=20)
    Text = models.CharField(max_length=500)


class ProjectModel(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=1000)
    # Id = models.CharField(max_length=20)
    # TeacherId = models.CharField(max_length=20)
    GithubLink = models.CharField(max_length=100)
    AccessLevel = models.IntegerField()

    City = models.OneToOneField(CityModel, on_delete=models.CASCADE)
    Marks = models.ManyToManyField(MarkModel)
    Type = models.ManyToManyField(TypeModel)
