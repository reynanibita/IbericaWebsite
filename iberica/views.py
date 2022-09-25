from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Tourism

# Create your views here.
def index(request):
    resort_image=Tourism.objects.all()
    template = loader.get_template('iberica/index.html')
    return HttpResponse(template.render({"resort_image":resort_image}))