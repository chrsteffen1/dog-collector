from django.contrib import admin
from .models import Dog, Walks, Toy

# Register your models here.

admin.site.register(Dog)
admin.site.register(Walks)
admin.site.register(Toy)
