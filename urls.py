"""cinchtax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views

# from django.urls import path
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),

admin.site.site_header = "CinchTax Admin"
admin.site.site_title = "CinchTax Admin Portal"
admin.site.index_title = "Welcome to CinchTax  Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("about", views.about, name="about"),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('gstbill', views.gstbill, name='gstbill'),
    path('inventory',views.inventory,name='inventory'),
    path('Balancesheet',views.Balancesheet,name='Balancesheet'),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout/', views.logoutUser, name="logout")
]
