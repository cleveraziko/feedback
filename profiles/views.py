from django.shortcuts import render
from django.views.generic.base import TemplateView


class CreateProfileView(TemplateView):
    template_name = "profiles/create_profile.html"
    
    
    
    
