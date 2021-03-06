from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # mainform= SimpleCalculatorForm()
    # if mainform.is_valid():
    #     mpg = mainform.cleaned_data['mpg']
    #     distance = mainform.cleaned_data['distance']
    #     gasprice = mainform.cleaned_data['gasprice']
    # return render(request, 'account/dashboard.html', {'form': mainform})
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form=LoginForm()
    return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render((request, 'account/register_done.html', {'new_user': new_user}))
    else:
        user_form=UserRegistrationForm()
    return render(request, 'account/register_done.html', {'user_form': user_form})