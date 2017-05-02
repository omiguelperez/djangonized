from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    ended_date= models.DateTimeField()
    owner = models.ForeignKey(User)
    todo = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.owner, self.todo)
