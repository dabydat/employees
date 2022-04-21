from django.contrib import admin

from .models import Department

# Register your models here.
# admin.site.register(Department)


@admin.register(Department)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('id',
                    'name',
                    'short_name'
                    )
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
