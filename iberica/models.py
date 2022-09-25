from django.db import models

# Create your models here.
class Tourism(models.Model):
    resort_image=models.ImageField(upload_to="resorts_image/%y")
    resort_name=models.CharField(max_length=50)
    resort_description=models.TextField(max_length=500)
    def __str__(self) :
        return self.resort_image