from django.shortcuts import render,HttpResponse
from django.views.generic import (View, 
                                  CreateView, 
                                  UpdateView, 
                                  DeleteView,
                                  TemplateView, 
                                  ListView, 
                                  DetailView
                                  )
from rest_framework.views import APIView
from rest_framework.response import Response
import json
def home(request):
    return render(request, 'app/home.html', {'title':'Home'})

def about(request):
    return render(request, 'app/about.html', {'title': 'About'})


        
