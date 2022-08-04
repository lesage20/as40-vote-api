from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Proposition)
admin.site.register(Upvote)
admin.site.register(Downvote)
