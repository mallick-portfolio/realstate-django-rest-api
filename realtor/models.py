from django.db import models
from datetime import datetime
# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=100)
    biodata = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to='realtor')
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.name
