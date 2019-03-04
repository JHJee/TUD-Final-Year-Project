from django.db import models
from djongo import models

# Create your models here
class Example(models.Model):
    st_no = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('example_edit', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'example'

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name
