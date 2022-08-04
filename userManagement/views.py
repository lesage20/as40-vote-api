from django.shortcuts import render
from .serializers import ProfileSerializer
from rest_framework import viewsets
from .models import *
# Create your views here.


class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    # def get_queryset(self):
    #     username = self.request.auth.user.username if self.request.auth else self.request.user.username
    #     return Profile.objects.filter(username=username)
