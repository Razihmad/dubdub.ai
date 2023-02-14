from django.db import models

# Create your models here.
class Reminders(models.Model):
    work  = models.CharField(max_length=10000)
    dateTime = models.DateTimeField()
    status = models.CharField(max_length=100,choices=(("Incomplete","Incomplete"),("Complete","Complete")))
    