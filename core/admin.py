from django.contrib import admin
from core.models import todo
class todoadmin(admin.ModelAdmin):
    list_display=('task',)
admin.site.register(todo,todoadmin)
