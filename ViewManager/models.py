from django.db import models

# Create your models here.

class Reveil(models.Model):
    date = models.TimeField(auto_now=False, )