from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import PersonCreationForm

# Register your models here.
from .models import CityModel, TypeModel, MarkModel, ProjectModel, Person


class PersonAdmin(UserAdmin):
    model = Person
    add_form = PersonCreationForm

    list_display = ['email', 'username', 'access_level']
    fieldsets = (
        (
            None,
            {
                'fields':
                    ('access_level',)}
        ),
        *UserAdmin.fieldsets,

    )


admin.site.register(CityModel)
admin.site.register(TypeModel)
admin.site.register(MarkModel)
admin.site.register(ProjectModel)
admin.site.register(Person, PersonAdmin)
