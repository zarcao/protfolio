from django.shortcuts import render,get_object_or_404
from gallery.models import Gallery

def home(request):
    gallerys = Gallery.objects
    return render(request,'home.html',{'gallerys':gallerys})

def detail(request, gallery_id):
    gallerys = get_object_or_404(Gallery, pk=gallery_id,)
    return render(request, 'detail.html', {'gallerys': gallerys})