from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def post_list(request: HttpRequest):
    return render(request, 'blog/post_list.html', {})