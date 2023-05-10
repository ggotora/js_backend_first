from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
# Create your views here.
def index(request):
    # return HttpResponse('Eish')
    return render(request, 'API/index.html')

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer