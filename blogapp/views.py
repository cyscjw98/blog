from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    post = Post.objects
    return render(request, 'blogapp/home.html', {'post':post})
