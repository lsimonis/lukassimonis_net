from django.db import models

# Create your models here.
class Experience(models.Model):
  company = models.CharField(max_length=32)
  title = models.CharField(max_length=32)
  start_date = models.DateField()
  end_date = models.DateField(null=True, blank=True)
  description = models.CharField(max_length=1024)

  def start_year(self):
    return self.start_date.strftime('%Y')

  def end_year(self):
    return self.end_date.strftime('%Y')

  def __str__(self):
    return self.company

class Education(models.Model):
    school = models.CharField(max_length=32)
    degree = models.CharField(max_length=8)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    major = models.CharField(max_length=32)
    gpa = models.FloatField()
  def start_year(self):
    return self.start_date.strftime('%Y')

  def end_year(self):
    return self.end_date.strftime('%Y')

  def __str__(self):
    return self.school
