from django.shortcuts import render
from .models import Image
# Create your views here.

def index(request):
    image_list = Image.objects.all()
    return render(request, 'gallery/index.html', {
        'image_list': image_list
        })