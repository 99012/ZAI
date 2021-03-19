from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from django.utils import timezone

# Create your views here.


def home(request):
    return render(request, 'projects/home.html')


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            project = Project()
            project.title = request.POST['title']
            project.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                project.url = request.POST['url']
            else:
                project.url = 'http://' + request.POST['url']
            project.icon = request.FILES['icon']
            project.image = request.FILES['image']
            project.pub_date = timezone.datetime.now()
            project.user = request.user
            project.save()
            return redirect('home')
        else:
            return render(request, 'projects/create.html', {'error': 'All fields are required'})
    else:
        return render(request, 'projects/create.html')
