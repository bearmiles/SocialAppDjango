from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    try:
        if request.method == 'POST':
            fnm = request.POST.get('fnm')
            emailid = request.POST.get('emailid')
            pwd = request.POST.get('pwd')
            print(fnm, emailid, pwd)
            my_user = User.objects.create_user(fnm, emailid, pwd)
            my_user.save()
            user_model = User.objects.get(username=fnm)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            if my_user is not None:
                login(request, my_user)
                return redirect('/')
            return redirect('/loginn')

        #jesli get
        return render(request, 'signup.html')


    #trobuleshooting
    except Exception as e:
        invalid = "User already exists"
        print("Błąd:", e)  
        return render(request, 'signup.html', {'invalid': invalid})


def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/')
        invalid="Invalid credentials"
        return render(request,'loginn.html', {'invalid': invalid})
    return render(request, 'loginn.html')
    
@login_required(login_url='/login')
def logoutt(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image-upload')
        caption = request.POST['caption']
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')






def home(request):
    post = Post.objects.all().order_by('-created_at')
  
    context={
        'post': post,
        
    }
    return render(request,'main.html', context)