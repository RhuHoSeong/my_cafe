from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .serializers import MemuSerializer
from .models import Memu

class MemuViewSet(viewsets.ModelViewSet):
    queryset =  Memu.objects.all()
    serializer_class = MemuSerializer


# def memu(request):
#   memu = Memu.objects.all().values()
#   template = loader.get_template('all_memu.html')
#   context = {
#     'memu': memu,
#   }
#   return HttpResponse(template.render(context, request))
  
# def details(request, id):
#   memu = Memu.objects.get(id=id)
#   template = loader.get_template('details.html')
#   context = {
#     'memu': memu,
#   }
#   return HttpResponse(template.render(context, request))
  
# def main(request):
#   template = loader.get_template('main.html')
#   return HttpResponse(template.render())

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'fruits': ['Apple', 'Banana', 'Cherry'],   
#   }
#   return HttpResponse(template.render(context, request))

