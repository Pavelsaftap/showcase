from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

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


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'get_image', 'AccessLevel')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.ProjectImage.url} width="240" height="135"')

    get_image.short_description = 'Превью'


class MarkModelAdmin(admin.ModelAdmin):
    list_display = ('Name', 'UserId', 'Score')


admin.site.register(CityModel)
admin.site.register(TypeModel)
admin.site.register(MarkModel, MarkModelAdmin)
admin.site.register(ProjectModel, ProjectModelAdmin)
admin.site.register(Person, PersonAdmin)
