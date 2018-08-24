from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,WritePost,Contact
from django.utils import timezone
from .models import post,User,contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
# Create your views here.
#messages.error(request,'Invalid')

def Contact_me(request):
    if request.method == "POST":
        form = Contact(request.POST)
        #print("11111111111111111111111111111111111111111111111111111111111111111\n1111111111111111111\n1111111111111111111\n")
        if form.is_valid:
            form.save()
            messages.success(request,"Request has been received")
            return redirect('/Contact/')
    else:
        form = Contact()
    return render(request,'blog/contact.html',{'form':form})

def about(request):
    return render(request,'blog/about.html')

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
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'blog/sign_up.html', {'form': form})    

#def contact(request):
 #   return render(request,'blog/contact.html')



def get_user_details(request,email):
    user = User.objects.get(email=email)
    return render(request,'blog/index.html',{"user":user})
@login_required
def post_likes_add(request,user_id,id):
    user = User.objects.get(id=user_id)
    pst = post.objects.get(id=id)
    if pst.post_like.filter(id=user_id).exists():
        pst.post_like.remove(user)
    else:
        pst.post_like.add(user)
    Post = post.objects.all()    
    context = {'pst': Post}
    return render(request,'blog/index.html',context=context)            

@login_required
def delete_post(request,id,user_id):
    del_ob = post.objects.get(id=id)
    if (del_ob.post_author.id == user_id):
        del_ob.delete()    
    pst = post.objects.all()
    return render(request,'blog/index.html',{'pst':pst})

def post_new(request):
    if request.method == "POST":
        form = WritePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.post_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = WritePost()
    return render(request,'blog/post_edit.html', {'form': form})   
