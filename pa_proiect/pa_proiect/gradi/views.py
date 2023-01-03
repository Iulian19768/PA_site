from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .models import AddBook,Inscrieri
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')
    
def test(request):

    if request.method == 'POST':
        author = request. POST['author']
        book_title = request. POST['title']
        description = request. POST['desc'] 
        new_book = AddBook (author=author, title=book_title, description=description)
        new_book.save()

    return render(request, 'test.html')
@login_required
def formular(request):
    
    if request.method == 'POST':

        nume = request. POST['Nume']
        prenume = request. POST['Prenume']
        sex = request. POST['Sex']
        email = request. POST['email']
        nr_tel = request. POST['nr_tel']
        adresa = request. POST['Adresa']
        cod_postal = request. POST['cod_postal']

        new_book = Post (nume=nume, prenume=prenume, sex=sex,email=email ,numar_tel=nr_tel, adresa=adresa,codpostal=cod_postal)
        new_book.save()
        


    return render(request, 'inscriere2.html',{})

@login_required
def insc(request):

    if request.method == 'POST':
        numep = request. POST['NumeParinte']
        adresa = request. POST['Adresa']
        codpostal = request. POST['CodPostal']
        nrtel = request. POST['NrTel']
        email = request. POST['Email']
        cnpp = request. POST['Cnpparinte']
        numec = request. POST['NumeCopil']
        initiala = request. POST['InitialaTata']
        cnpc = request. POST['Cnpcopil']

        new = Inscrieri(numeparinte=numep, adresa= adresa,
                        codpostal=codpostal, nrtel=nrtel, email=email,
                        cnpparinte=cnpp, numecopil=numec, initiala =initiala,
                        cnpcopil=cnpc)
        new.save()

    return render(request, 'inscriere.html')

def log(request):
    if request.method == 'POST':
        username= request.POST.get('User_name')
        password= request.POST.get('Password')
        
        validade_user = authenticate(request, username=username, password=password)
        if validade_user is not None:
            login(request, validade_user)
            return redirect('gradi-inscriere2') 
        else:
            messages.error(request, 'Date incorecte, sau contul nu exista')
            #return redirect('gradi-inscriere2')   
    return render(request, 'login.html',{})

def reg(request):
    if request.method == 'POST':
        First_name= request.POST.get('First_name')
        Last_name= request.POST.get('Last_name')
        name= request.POST.get('User_name')
        email= request.POST.get('Email')
        password= request.POST.get('Password')
        password2= request.POST.get('password2')

        if(password!=password2):
            messages.error(request,'Parolele nu se potrivesc')
            return redirect('gradi-register')

        get_all_users_by_username = User.objects.filter(username=name)
        if get_all_users_by_username:
            messages.error(request, 'Numele de utilizator este deja utilizat')
            return redirect('gradi-register')

        new_user = User.objects.create_user(username=name, email=email, password=password)
        new_user.first_name = First_name
        new_user.last_name = Last_name
        new_user.save()
        #messages.success(request,'Cont creat!')
        return redirect('gradi-login')
    return render(request, 'register.html',{})

def logoutuser(request):
    logout(request)
    return redirect('gradi-login')