from django.db import models
from django.urls import reverse



  
class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

	# new code below
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("dogs_detail", kwargs={"dog_id": self.id})

class Walks(models.Model):
  date = models.DateField('Walking date')
  miles = models.IntegerField()
  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

