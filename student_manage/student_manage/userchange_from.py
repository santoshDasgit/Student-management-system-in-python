from django import forms
from server.models import User
from django.contrib.auth.forms import UserChangeForm

class UserChange_form(UserChangeForm):
    class Meta:
        model=User
        fields = ['profile_image','first_name','last_name','email']
        
