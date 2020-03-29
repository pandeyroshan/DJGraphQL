from django.db import models
from django.utils import timezone
# Create your models here.

class ToDoList(models.Model):
    heading = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    created_on = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Task '+str(self.id)
    
    class Meta:
        verbose_name = 'To Do'
        verbose_name_plural = 'To Do'