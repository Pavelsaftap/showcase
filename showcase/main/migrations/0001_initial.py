# Generated by Django 3.2.3 on 2021-06-03 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MarkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('UserId', models.CharField(max_length=20)),
                ('Text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=1000)),
                ('GithubLink', models.CharField(max_length=100)),
                ('AccessLevel', models.IntegerField()),
                ('City', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.citymodel')),
                ('Marks', models.ManyToManyField(to='main.MarkModel')),
                ('Type', models.ManyToManyField(to='main.TypeModel')),
            ],
        ),
    ]