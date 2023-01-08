from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def Pagelogin(request):
    if request.user.is_authenticated:
        return redirect ("/penangkaran/")
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('pass')
            user=authenticate(request, username=username, password=pass1)
            if user is not None:
                login(request, user)
                return redirect('/penangkaran/')
            
        return render(request, "login.html")

def Pagesignup(request):
    if request.user.is_authenticated:
        return redirect ("/penangkaran/")
    else:
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
            my_user=User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('/login/')

        return render(request, "signup.html")

def Pagelogout(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='login')
def penangkaran(request):
      kandang = Penangkaran.objects.all()
      tempat_json = serializers.serialize('json', kandang)
      data = {
          "judul"   : "penangkaran",
          'kandang'  : kandang,
          'tempat_json' : tempat_json,
      }
      return render(request, "penangkaran.html", data)

@login_required(login_url='login')
def tambah_penangkaran(request):
      if request.POST:
          form = FormPenangkaran(request.POST)
          if form.is_valid():
              form.save()
              form = FormPenangkaran()
              kandang = Penangkaran.objects.all()
              data = {
                  "judul"   : "Tambah Data",
                 'Title' : "Input Data",
                 'kandang' : kandang,
                 'form'    : form,
                 'pesan'   : "Data berhasil ditambahkan"
              }
              return render(request, "tambah_penangkaran.html", data)
      else:
          form  = FormPenangkaran()
          kandang = Penangkaran.objects.all()
          data = {
             "judul"   : "Tambah Data",
             'Title'   : "Input Data",
             'kandang' : kandang,
             'form'    : form,
          }
          return render(request, "tambah_penangkaran.html", data)

@login_required(login_url='login')
def edit_penangkaran(request, id):
      kandang = Penangkaran.objects.get(pk=id)
      if request.POST:
          form = FormPenangkaran(request.POST,instance=kandang)
          if form.is_valid():
              form.save()
              data = {
                  "judul"   : "Edit Data",
                  'Title' : "Edit Data",
                  'kandang' : kandang,
                  'form'  : form,
                  'pesan' : "Data berhasil diubah"
              }
              return render(request, "edit_penangkaran.html", data)
      else:
          form = FormPenangkaran(instance=kandang)
          data = {
          "judul"   : "Edit Data",
          'Title' : "Edit Data",
          'kandang' : kandang,
          'form'  : form,
           }
      return render(request, "edit_penangkaran.html", data)

def delete_penangkaran(request, id):
    kandang = Penangkaran.objects.get(pk=id)
    kandang.delete()
    
    return redirect("/penangkaran/")

@login_required(login_url='login')
def data_penyu(request):
      penyu = Data.objects.all()
      data = {
          "judul" : "penangkaran",
          'penyu' : penyu,
      }
      return render(request, "data_penyu.html", data)

@login_required(login_url='login')
def tambah_data(request):
      if request.POST:
          form = FormPenyu(request.POST, request.FILES)
          if form.is_valid():
              form.save()
              form = FormPenyu()
              penyu = Data.objects.all()
              data = {
                  "judul" : "Tambah Data",
                 'Title' : "Input Data",
                 'penyu' : penyu,
                 'form'  : form,
                 'pesan' : "Data berhasil ditambahkan"
              }
              return render(request, "tambah_data.html", data)
      else:
          form  = FormPenyu()
          penyu = Data.objects.all()
          data = {
             "judul" : "Tambah Data",
             'Title' : "Input Data",
             'penyu' : penyu,
             'form'  : form,
          }
          return render(request, "tambah_data.html", data)

@login_required(login_url='login')
def edit_data(request, id):
      penyu = Data.objects.get(pk=id)
      if request.POST:
          form = FormPenyu(request.POST, request.FILES, instance=penyu)
          if form.is_valid():
              form.save()
              data = {
                  "judul"   : "Edit Data",
                  'Title' : "Edit Data",
                  'penyu' : penyu,
                  'form'  : form,
                  'pesan' : "Data berhasil diubah"
              }
              return render(request, "ubah_data.html", data)
      else:
          form = FormPenyu(instance=penyu)
          data = {
          "judul"   : "Edit Data",
          'Title' : "Edit Data",
          'penyu' : penyu,
          'form'  : form,
           }
      return render(request, "ubah_data.html", data)

def delete_data(request, id):
    penyu = Data.objects.get(pk=id)
    penyu.delete()
    
    return redirect("/data_penyu/")