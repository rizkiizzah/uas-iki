"""penangkaran URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from penangkaran_app.views import *
from penangkaran_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.Pagelogin, name='login'),
    path("logout/", views.Pagelogout, name='logout'),
    path("signup/", views.Pagesignup, name='signup'),
    path("penangkaran/", penangkaran),
    path("tambah_penangkaran/", tambah_penangkaran),
    path("penangkaran/edit_penangkaran/<int:id>", edit_penangkaran, name='edit_1'),
    path("penangkaran/delete_penangkaran/<int:id>", delete_penangkaran),
    path("data_penyu/", data_penyu),
    path("tambah_data/", tambah_data),
    path("data_penyu/edit_2/<int:id>", edit_data, name='edit_2'),
    path("data_penyu/delete_data/<int:id>", delete_data),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
