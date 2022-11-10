from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog, Toy
from .forms import WalkingForm
from django.views.generic import ListView, DetailView

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy


class DogCreate(CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']
  
class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'
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
  toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
  walking_form = WalkingForm()
  return render(request, 'dogs/detail.html', { 'dog': dog, 'walking_form': walking_form, 'toys': toys_dog_doesnt_have  })

def add_walking(request, dog_id):
  form = WalkingForm(request.POST)
  if form.is_valid():
    new_walking = form.save(commit=False)
    new_walking.dog_id = dog_id
    new_walking.save()
  return redirect('dogs_detail', dog_id=dog_id)