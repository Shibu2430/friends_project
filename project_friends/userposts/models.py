from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Postings(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField()
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', default=None, blank=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.likes.all().count()

LIKE_CHOICES = {
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
}

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Postings, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)
