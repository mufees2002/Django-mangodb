from django.db import models

# Create your models here.
import mongoengine
mongoengine.connect(db="db_name", host="hostname", username="username", password="pwd")