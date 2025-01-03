from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
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

        # Jeśli metoda to GET, renderuj formularz rejestracji
        return render(request, 'signup.html')

    except Exception as e:
        invalid = "User already exists"
        print("Błąd:", e)  # Dodaj logowanie błędów, aby lepiej diagnozować problemy
        return render(request, 'signup.html', {'invalid': invalid})

def home(request):
    return HttpResponse("Hello")