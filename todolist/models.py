from django.db import models

class Todolist(models.Model):
    text = models.CharField(max_length=40)
    completed = models.BooleanField(False)


    def __str__(self):
        return self.text