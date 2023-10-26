"""
URL configuration for dance_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# urls.py
from django.contrib import admin
from django.urls import path
from danceapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sp, name='sp'),
    path('admission/', views.admission, name='admission'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('sp/', views.sp, name='sp'),
    path('admin1/',views.admin1, name='admin1'),
    path('profile/',views.profile, name='profile'),
    path('gallery/',views.gallery, name='gallery'),
    path('insertuser/', views.insertuser, name='insertuser'),
    path('emt/',views.emt, name='emt'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('get_secret_credentials/', views.get_secret_credentials, name='get_secret_credentials'),
    path('logout/', views.logout_view, name='logout'),
]
