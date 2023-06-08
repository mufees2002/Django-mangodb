from django.db import models


class Info(models.Model):
     Name=models.CharField(max_length=200)
     Age=models.CharField(max_length=200)
     Phone=models.IntegerField()




