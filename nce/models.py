from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20)


class Project(models.Model):
    title = models.CharField(max_length=270)
    contents = models.TextField()
    numbers_of_pages = models.IntegerField()
    departments = models.ManyToManyField('Department', related_name='projects')

    def __str__(self):
        return self.title

