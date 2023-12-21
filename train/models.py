from django.db import models

class Station(models.Model):
    pic = models.ImageField()
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=20, choices = [
        ('TEH', 'Tehran'),
        ('SRI', 'Sari'),
        ('ISF', 'Isfahan'),
    ])
    address = models.TextField(max_length=1000)
    phone_number = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self) -> str:
        return self.name

class Train(models.Model):
    origin = models.ForeignKey(Station, on_delete=models.CASCADE)
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='Des')
    date_time = models.DateTimeField()
    no = models.CharField(max_length=20)
    capacity = models.IntegerField()
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.origin.city} - {self.destination.name}"