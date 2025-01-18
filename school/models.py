from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

class Section(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Class(models.Model):
    name = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
