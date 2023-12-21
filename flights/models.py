from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=255)
    no = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.TextField(max_length=1000)
    phone_number = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self) -> str:
        return self.name

class flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='Des')
    name = models.CharField(max_length=255)
    no = models.CharField(max_length=20)
    capacity = models.IntegerField()
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'flight' 
        

