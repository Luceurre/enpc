from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

# Affiche l'ensemble des sections dispos.
from .models import File, Section


def index(request):
    return sections(request)

#
def sections(request):
    return HttpResponse("L'ensemble des sections.")

def files(request, section):
    try:
        section_id = Section.objects.get(name = section).id
        files = File.objects.filter(section_id = section_id)
    except:
        files = []


    test = ""
    for file in files:
        test += "<a href=%s> test </a>" % file.file.url

    return HttpResponse(test)