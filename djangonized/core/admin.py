from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('owner', 'todo', 'done',)
    exclude = ('onwer',)

    def save_model(self, request, obj, form, change):
        obj.onwer = request.user
        obj.save()

admin.site.register(Todo, TodoAdmin)
