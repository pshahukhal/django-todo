from django.db import models

# Model defined for storing the to do items
class ToDoItems (models.Model):
    id =  models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    content = models.TextField(blank=True)
    completed = models.BooleanField(default= False)

    def __str__(self):
        return self.title