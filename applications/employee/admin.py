from django.contrib import admin
from .models import Employee, Skills

# Register your models here.


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    '''Admin View for Skills'''

    list_display = ('id', 'skill', )


@admin.register(Employee)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('id',
                    'name',
                    'last_name',
                    'age',
                    'id_number',
                    'job_name',
                    'department_name',
                    )

    def department_name(self, obj):
        return obj.department.name
