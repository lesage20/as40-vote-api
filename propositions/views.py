from django.shortcuts import render
from .models import Proposition, Upvote, Downvote
# Create your views here.
from rest_framework import viewsets
from .serializers import *


class PropViewset(viewsets.ModelViewSet):
    serializer_class = PropSerializer
    queryset = Proposition.objects.all().order_by('-id')


class UpvoteViewset(viewsets.ModelViewSet):
    serializer_class = UpvoteSerializer
    queryset = Upvote.objects.all()


class DownvoteViewset(viewsets.ModelViewSet):
    serializer_class = DownvoteSerializer
    queryset = Downvote.objects.all()
