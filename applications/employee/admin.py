from django.contrib import admin
from .models import Employee, Skills

# Register your models here.
admin.site.register(Skills)


@admin.register(Employee)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name',
                    'last_name',
                    'age',
                    'id_number',
                    'job_name',
                    'department_name',
                    )

    def department_name(self, obj):
        return obj.department.name
    # list_filter = ('',)
    # inlines = []
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
