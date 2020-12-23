from django.shortcuts import render, redirect
from employee import forms
from employee.models import BranchDetails
from django.http import HttpResponseRedirect, HttpResponse
#
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'employee/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def employee(request):
    form = forms.EmployeeInputForms

    if request.method == 'POST':
        form = forms.EmployeeInputForms(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    return render(request, 'employee/employee.html', {'form': form})


def branch(request):
    form = forms.BranchDetailsForms

    if request.method == 'POST':
        form = forms.BranchDetailsForms(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('emp:branch')

    return render(request, 'employee/branch.html', {'form': form})


def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileForm()

    return render(request, 'employee/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Your Account not Active!')
        else:
            print("Someone Tried to Login and Failed!")
            print(f"username: {username} Password: {password}")
            return HttpResponse("Invalid Login Details Supplied!")
    else:
        return render(request, 'employee/login.html', {})
