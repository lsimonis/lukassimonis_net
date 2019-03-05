from django.db import models

# Create your models here.
class Experience(models.Model):
  company = models.CharField(max_length=50)
  startdate = models.CharField(max_length=20)	#Could use DateField, but want to leave this value flexible for now. 
  enddate = models.CharField(max_length=20)
  description = models.CharField(max_length=1000)

  def __str__(self):
    return self.company
