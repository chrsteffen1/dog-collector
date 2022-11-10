from django.forms import ModelForm
from .models import Walks

class WalkingForm(ModelForm):
  class Meta:
    model = Walks
    fields = ['date', 'miles']