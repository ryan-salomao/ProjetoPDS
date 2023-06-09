"""
URL configuration for project project.

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
from django.contrib import admin
from django.urls import path
from app.views import home, form, home1, form1, create, createuser, view, geo, geo_result, index1, favoritos, favoritar, desfavoritar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', createuser, name='form'),
    path('home1/', home1, name='home1'),
    path('form1/', form1, name='form1'),
    path('create/', create, name='create'),
    path('createuser/', createuser, name='createuser'),
    path('index1/', index1, name='index1'),
    path('view/<int:pk>/', view, name='view'),
    path('geo/', geo, name='geo'),
    path('geo/<int:pk>/', geo_result, name='geo_result'),
    path('favoritar/<int:pk>', favoritar, name='favoritar'),
    path('desfavoritar/<int:pk>', desfavoritar, name='desfavoritar'),
    path('favoritos/', favoritos, name='favoritos'),
]
