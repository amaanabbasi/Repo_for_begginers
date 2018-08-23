from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
from .models import Items

# Create your views here.
@csrf_exempt
def read(request):
    data = [item.json() for item in Items.objects.all()]
    return JsonResponse(data, safe=False)

@csrf_exempt
def create(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    text = body['text']
    complete = False
    i = Items(text=text, complete=complete)
    i.save()
    return read(request)

@csrf_exempt
def update(request, todoID):
    i = get_object_or_404(Items, pk=todoID)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    i.text = body['text']
    i.complete = body['complete']
    i.save()
    return read(request)

@csrf_exempt
def delete(request, todoID):
    i = get_object_or_404(Items, pk=todoID).delete()
    return read(request)
