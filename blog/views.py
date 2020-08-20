from django.shortcuts import render, get_object_or_404
from .models import blog
# Create your views here.
def home(request):
    blogs= blog.objects.order_by('-date')

    return render( request ,'blog/all_blogs.html',{'blogdict':blogs})

def detail(request, blog_id):
    detailedblog = get_object_or_404(blog,pk=blog_id)
    return render(request , 'blog/blog_details.html', {'dblog':detailedblog})