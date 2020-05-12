from django.shortcuts import render, redirect
from django.http import HttpResponse

from userposts.models import Postings, Like

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def feeds(request):

    posting = Postings.objects.order_by('-list_date')
    user = request.user
    context = {
        'posting' : posting,
        'user' : user
    }
    return render(request, 'accounts/feeds.html', context)

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Postings.objects.get(id=post_id)

        if user in post_obj.likes.all():        #if user is actually liked the post
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)
        
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

    return redirect('feeds')








