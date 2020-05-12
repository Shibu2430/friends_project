from django.contrib import admin

from .models import Postings, Like


# Register your models here.

admin.site.register(Postings)
admin.site.register(Like)