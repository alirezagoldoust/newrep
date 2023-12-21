from django.db import models

class Terminal(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=20)
    address = models.TextField(max_length=1000)
    phone_number = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()

class Travel(models.Model):
    origin = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    no = models.CharField(max_length=20)
    capacity = models.IntegerField()
    price = models.FloatField()