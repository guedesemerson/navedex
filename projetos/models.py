from django.db import models
from django.contrib.auth.models import User
from navers.models import Naver


class Projetos(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    navers = models.ManyToManyField(Naver)
