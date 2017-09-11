from django.shortcuts import render # for image
from django.http import HttpResponse # for http response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Photo
from .forms import PhotoForm

# Create your views here.
def hello(request):
    return HttpResponse("Hello, world !!")

def detail(request, pk, hidden=False):
    photo = get_object_or_404(Photo, pk=pk)

    messages = (
            '<p>{pk} is showed</p>'.format(pk=photo.pk),
            '<p>Your address {url}</p>'.format(url=photo.image.url),
            '<p><img src="{url}" /></p>'.format(url=photo.image.url),
        )
    return HttpResponse('\n'.join(messages))

def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect(obj) # call modles.py: get_absolute_url

    ctx = {
        'form': form,
    }

    return render(request, 'edit.html', ctx)