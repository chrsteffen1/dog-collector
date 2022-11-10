from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from .forms import WalkingForm


class DogCreate(CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']
  
class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'
# Create your views here.


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs})

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  walking_form = WalkingForm()
  return render(request, 'dogs/detail.html', { 'dog': dog, 'walking_form': walking_form })

