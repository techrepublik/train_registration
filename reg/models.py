from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    subject_code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=255)
    units = models.IntegerField()

    def __str__(self):
        return f"{self.subject_code} - {self.title}"


class Student(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    SEX = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    id_no = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField(auto_now_add=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=10, choices=SEX, blank=True, null=True)
    subjects = models.ManyToManyField(Subject, related_name='students')

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"
