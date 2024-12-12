from django.db import models

# Create your models here.
class Person(models.Model):
    
    name = models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    
    address=models.TextField()

    photo = models.ImageField(upload_to='person/', blank=True, null=True)

    def __str__(self):
        return self.name