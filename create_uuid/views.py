from django.shortcuts import render
from django.http import HttpResponse
import uuid
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return HttpResponse('This is my first application')

def abc(request):
    return render(request, 'index.html')
    
def mulUuid(request):
    index = request.GET.get('index', 0)
    index = int(index)
    list = []
    for i in range(index):
        temp = uuid.uuid4()
        s = str(temp).split('-')
        s = ''.join(s)
        list.append(s[:20])
    return JsonResponse({ 'uuidList': list })