from django.shortcuts import render, redirect

from core.views import index
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings



# Create your views here.
User = settings.AUTH_USER_MODEL

New = get_user_model()
def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if New.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists")
            return render(request, 'userauths/sign-up.html', {'form':form})

        if password1 != password2:
            messages.error(request, "The two password fields didn’t match.")
            return render(request, 'userauths/sign-up.html', {'form': form})

        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect("core:index")

    else:
        form = UserRegisterForm()


    form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, "userauths/sign-up.html", context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey you are already logged in.")
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password1")

        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"User with {email} does not exists")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect("core:index")
        else:
            messages.warning(request, "User Does Not Exist. Create an account.")

    context = {

    }

    return render(request, "userauths/sign-in.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("userauths:sign-in")