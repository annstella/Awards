from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
def welcome(request):
   return render(request, 'all-task/index.html')

def task(request):
   task = Image.objects.all()

   return render(request, 'all-task/index.html', {"task":task})