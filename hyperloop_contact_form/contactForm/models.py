from django.db import models

# Create your models here.
class ContactDetail(models.Model):
    Name = models.CharField(max_length=256)
    Email = models.EmailField()
    Roll = models.CharField(max_length=256)
    Phone = models.IntegerField()
    Dept = models.CharField(max_length=256)
    SubC = models.BooleanField()
    SubS = models.BooleanField()
    SubE = models.BooleanField()
    SubA = models.BooleanField()
    SubP = models.BooleanField()
    Comments = models.CharField(max_length=256)

    def __str__(self):
        return self.Name
