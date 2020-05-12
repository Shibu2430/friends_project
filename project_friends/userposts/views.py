from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Postings, Like
# Create your views here.

def addpost(request):
    if request.method == 'POST' :
        title = request.POST['title']
        photo = request.FILES['photo']
        description = request.POST['description']
        
        postings = Postings(title=title, photo=photo, description=description)
        postings.save()

        messages.success(request, 'New post added..')
        return redirect('index')
    else:
        return render(request, 'accounts/addpost.html')
