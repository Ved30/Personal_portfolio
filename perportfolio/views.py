from django.shortcuts import render,get_object_or_404
from .models import project, skills , experience
from blog.models import blog
# Create your views here.
def home(request):
    projects = project.objects.all()
    skill = skills.objects.all()
    exp = experience.objects.all()
    blo= blog.objects.all()[:2]
    return render(request, 'perportfolio/index.html', {'proj': projects , 'skill' : skill ,'ep':exp, 'blogs':blo } )