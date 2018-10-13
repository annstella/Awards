from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request,'indexx.html')

# def task(request):
#    task = Image.objects.all()

#    return render(request, 'all-task/index.html', {"task":task})

def search_results(request):
  
    if 'projects' in request.GET and request.GET["projects"]:
        category = request.GET.get("projects")
        searched_categories = Image.search_image(category)
        message = f"{category}"

        return render(request, 'all-task/search.html',{"message":message,"projects": searched_categories})

    else:
        message = " Found 0 images for the search term"
        return render(request, 'all-task/search.html',{"message":message})
