from django.shortcuts import render
from .forms import profilecreationsform,usercreateprofile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def dash(request):
    return render(request, 'screen/dash.html')


def test_login(request):
    login_form = AuthenticationForm()
    return render(request, 'screen/login.html',{'form':login_form})


def signup(request):
    if request.method == 'POST':
        form = usercreateprofile(request.POST)
        if form.is_valid():
            user = User.objects.create(username = request.POST['email_professional'],password = request.POST['password'])
            Profile.objects.create(user=user,nom = 'fsd',prenom='fre',numero_du_telephone='rew')
    return render(request, 'screen/signup.html',{'form':usercreateprofile})

def test_logout(request):
    return render(request, 'screen/dash.html')