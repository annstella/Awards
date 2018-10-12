from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request,'indexx.html')

# def task(request):
#    task = Image.objects.all()

#    return render(request, 'all-task/index.html', {"task":task})