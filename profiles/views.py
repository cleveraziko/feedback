from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)



class CreateProView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profile"


#Bu eski usul tepadaki CreateView oson va qulay
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request,"profiles/create_profile.html",{
#             "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES['user_image'])
#             profile.save()
#             # store_file(request.FILES['image'])
#             return HttpResponseRedirect("/profile")
#         else:
#             return render(request,"profiles/create_profile.html",{
#             "form": submitted_form  
#         })

    

class ProfileView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"

    

    
    
