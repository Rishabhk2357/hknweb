from django.contrib import admin
from .models import Alumnus


class AlumnusAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'perm_email', 'mailing_list',
              'grad_season', 'grad_year', 'grad_school', 'job_title',
              'company', 'salary', 'city', 'country_state', 'suggestions']
    list_display = ('first_name', 'last_name', 'perm_email')
    list_filter = ['grad_year', 'mailing_list', 'created_at',
                   'updated_at', 'country_state']
    search_fields = ['first_name', 'last_name', 'perm_email', 'grad_school']


admin.site.register(Alumnus, AlumnusAdmin)

