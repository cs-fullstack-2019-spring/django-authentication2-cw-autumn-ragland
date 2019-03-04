from django.shortcuts import render
from .models import BlogModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# login
def index(request):
    return render(request, "cwApp/index.html")

# render posts by username
@login_required
def myPosts(request):
    post_list = BlogModel.objects.filter(username=request.user)
    context = {
        'post_list': post_list
    }
    return render(request, 'cwApp/myPosts.html', context)

