from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Add the Toy model
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})
  
class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

	# new code below
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("dogs_detail", kwargs={"dog_id": self.id})
  


class Walks(models.Model):
  date = models.DateField('Walking date')
  miles = models.IntegerField()
  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
  
class Meta:
  ordering = ['-date']


