from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import requests, json

# Create your views here.

# Affiche l'ensemble des sections dispos.
from django.template import loader

from .models import File, Section


def index(request):
    return sections(request)


def sections(request):
    data = json.loads(requests.get("http://127.0.0.1:8000/files/api/sections").text)
    template  = loader.get_template('files/sections.html')
    context = {
        'sections': data['sections']
    }

    return HttpResponse(template.render(data, request))

def files(request, section):
    return HttpResponse("Ur in section %s" % section)
#
def api_sections(request):
    data = {
        'sections': []
    }

    section_objects = Section.objects.all()

    for section in section_objects:
        data['sections'].append({'name': section.name, 'url': section.url})

    return JsonResponse(data)

def api_files(request, section):
    try:
        section_id = Section.objects.get(name = section).id
        files = File.objects.filter(section_id = section_id)
    except:
        files = []


    data = {
        'files': []
    }

    for file in files:
        data['files'].append(
            {
                'name': file.name,
                'url': file.file.url,
                'type': file.type.name
            }
        )

    return JsonResponse(data)