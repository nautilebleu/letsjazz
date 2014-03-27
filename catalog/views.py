from django.shortcuts import render_to_response

from models import Artist
# Create your views here.

def home(request):
    artists = Artist.objects.filter(name__icontains='y', is_band=True)
    return render_to_response('catalog/home.html', {
        'name': 'Goulwen',
        'artists': artists
    })
