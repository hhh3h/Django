from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Photo

# Create your views here.
def hello(request):
    return HttpResponse("Hello, world !!")

def detail(request, pk):

    photo = get_object_or_404(Photo, pk=pk)

    messages = (
            '<p>{pk} is showed</p>'.format(pk=photo.pk),
            '<p>Your address {url}'.format(url=photo.image.url)
        )
    return HttpResponse('\n'.join(messages))