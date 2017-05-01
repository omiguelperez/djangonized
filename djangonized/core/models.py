from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_finalizado = models.DateTimeField()
    propietario = models.ForeignKey(User)
    todo = models.TextField()
    hecho = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.propietario, self.todo)
