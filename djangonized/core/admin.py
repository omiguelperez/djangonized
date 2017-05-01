from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'todo', 'hecho',)
    exclude = ('propietario',)

    def save_model(self, request, obj, form, change):
        obj.propietario = request.user
        obj.save()

admin.site.register(Todo, TodoAdmin)
