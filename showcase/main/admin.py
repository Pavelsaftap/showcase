from django.contrib import admin

# Register your models here.
from .models import CityModel, TypeModel, MarkModel, ProjectModel

admin.site.register(CityModel)
admin.site.register(TypeModel)
admin.site.register(MarkModel)
admin.site.register(ProjectModel)