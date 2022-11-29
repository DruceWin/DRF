from django.shortcuts import render

from .tasks import summ


# Create your views here.

def get_page(request):
    summ.delay()
    return render(request, 'index.html')
