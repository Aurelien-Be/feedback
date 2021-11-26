from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect 
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from django.urls import reverse

from . forms import ProfileForm
from .models import UserProfile

# Create your views here.


#class CreateProfileView(View):
#    def get(self, request):
#        form = ProfileForm()
#        return render(request, "profiles/create_profile.html", {
#            "form" : form
#        })

#    def post(self, request):
#        submitted_form = ProfileForm(request.POST, request.FILES)

#        if submitted_form.is_valid():
#          profile = UserProfile(image=request.FILES["user_image"]) #user image as in the template wich uses forms, wich uses user_image as a filename 
#          profile.save()
#          return HttpResponseRedirect("/profiles")
#        
#        return render(request, "profiles/create_profile.html", {
#            "form" : submitted_form
#        })

#shorter with createview 
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "theprofiles"

