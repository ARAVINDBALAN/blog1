from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,post,contact   
class SignUpForm(UserCreationForm):
    #USERNAME_FIELD = 'email'
    class Meta:
        model = User
        fields = ('email','first_name','last_name','avatar','password1','password2')


class WritePost(forms.ModelForm):
    class Meta:
        model = post
        fields = ('post_text','post_title',)

class Contact(forms.ModelForm):
        class Meta:
            model = contact
            fields = ('name','email','phone','messages',)
                    