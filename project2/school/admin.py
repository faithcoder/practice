from django.contrib import admin
from school.models import Notice, Branch, Profile
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class NoticeAdmin(ModelAdmin):
    list_display = ['subject', 'cr_date']
    search_fields = ['subject', 'msg']
    list_filter = ['cr_date']

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Branch)
admin.site.register(Profile)