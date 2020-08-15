from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse
# Create your views here.

def hello(self):
    return HttpResponse('Helloworld')