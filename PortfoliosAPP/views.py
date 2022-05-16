from django.shortcuts import render ,get_object_or_404
from .models import Project
# Create your views here.
def home(request):
    projects =Project.objects.all()
    return render (request,'Portfolio/home.html',{'projects':projects})
def detail(request,idProjet):
    project=get_object_or_404(Project,pk=idProjet)
    return render (request,'Portfolio/detail.html',{'project':project})

def test(request):
    projects =Project.objects.all()
    return render (request,'Portfolio/test.html',{'projects':projects})

  