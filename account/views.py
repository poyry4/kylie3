from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import image, category, product 
from django.contrib.auth.decorators import login_required
from . import forms

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('account:adminKylie')
    else:
        form = AuthenticationForm()
        return render(request, 'account/login.html', { 'form': form })
 
def logoutView(request):
    if request.method == 'POST':
            logout(request)
            return redirect('account:login')

@login_required(login_url="/account/login/")
def adminKylie(request):
    adminKylie = category.objects.all()
    return render(request, 'account/adminKylie.html', { 'adminKylie': adminKylie }) 

@login_required(login_url="/account/login/")
def category_create(request):
    if request.method == 'POST':
        form = forms.category_create(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.save()
            return redirect('account:category_create')
    else:
        form = forms.category_create()
    return render(request, 'account/category_create.html', { 'form': form })