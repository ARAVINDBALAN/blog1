from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,WritePost
from django.utils import timezone
from .models import post
# Create your views here.
def home(request):
    pst = post.objects.all()
    return render(request,'blog/index.html',{'pst':pst})



def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            #login(request, user)
            return redirect('/home/')
    else:
        form = SignUpForm()
    return render(request, 'blog/sign_up.html', {'form': form})    

def get_user_details(request,email):
    user = User.objects.get(email=email)
    return render(request,'blog/index.html',{"user":user})

def post_new(request):
    if request.method == "POST":
        form = WritePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.post_date = timezone.now()
            post.save()
            return redirect('/home/', pk=post.pk)
    else:
        form = WritePost()
    return render(request, 'blog/post_edit.html', {'form': form})   