from django.shortcuts import render,redirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm
from .forms import NewProjectsForm
from .models import Profile , Projects


# Create your views here.
@login_required(login_url='/accounts/login')
def welcome(request):
    task = Projects.objects.all() 
    return render(request,'indexx.html', locals())

# def task(request):
#    task = Image.objects.all()

#    return render(request, 'all-task/index.html', {"task":task})

def search_results(request):
  
    if 'username' in request.GET and request.GET["projects"]:
        category = request.GET.get("projects")
        searched_categories = Projects.search_project(category)
        message = f"{category}"

        return render(request, 'all-task/search.html',{"message":message,"projects": searched_categories})

    else:
        message = " Found 0 projects for the search term"
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

@login_required(login_url='/accounts/login/')
def profile(request, user_username = None):
    if user_username == None:
        user = request.user
    else:
        user = get_object_or_404( User ,username = user_username)
    
    profile = Profile.get_user_profile( user )
    title = "Profile"
    projects = Projects.get_projects_by_id(user.id)
    print(projects)

    context = {
        'title':title, 
        "projects":projects,
        "profile" : profile }
        
    return render(request, 'profile/profile.html',context)


@login_required(login_url='/accounts/login/')
def new_projects(request):
    profile = Profile.objects.all()
    for profile in profile:
        current_user = request.user
        if request.method == 'POST':
            projects_form = NewProjectsForm(request.POST, request.FILES)
            if projects_form.is_valid():
                projects = projects_form.save(commit=False)
                projects.user = current_user
                projects.profile = profile
                projects.save()
            return redirect('welcome')

        else:
            projects_form = NewProjectsForm()
    return render(request, 'new_projects.html', {"projects_form": projects_form})