from django.shortcuts import render
from gallery.models import Gallery

def home(request):
    gallerys = Gallery.objects
    return render(request,'home.html',{'gallerys':gallerys})

def detail(request, gallery_id):
    gallerys = Gallery.objects.filter(id = gallery_id)
    print(gallerys)
    return render(request, 'detail.html', {'gallerys': gallerys})