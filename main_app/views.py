from django.shortcuts import render

from django.http import HttpResponse


class Dog:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Lolo', 'tabby', 'Kinda rude.', 3),
  Dog('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Dog('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Dog('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Create your views here.


def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs})