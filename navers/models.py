from django.db import models
from django.contrib.auth.models import User


class Naver(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    admission_date = models.DateField()
    job_role = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



