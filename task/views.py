from django.shortcuts import render
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


# Create your views here.
def welcome(request):
    return render(request,'indexx.html')

# def task(request):
#    task = Image.objects.all()

#    return render(request, 'all-task/index.html', {"task":task})

def search_results(request):
  
    if 'projects' in request.GET and request.GET["projects"]:
        category = request.GET.get("projects")
        searched_categories = Projects.search_image(category)
        message = f"{category}"

        return render(request, 'all-task/search.html',{"message":message,"projects": searched_categories})

    else:
        message = " Found 0 images for the search term"
        return render(request, 'all-task/search.html',{"message":message})


def task_today(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('task_today')
    else:
        form = NewsLetterForm()
    return render(request, 'indexx.html', {"projects":projects,"letterForm":form})