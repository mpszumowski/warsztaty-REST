"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from movies.views import (MoviesView, MovieView, PeopleView, PersonView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', MoviesView.as_view(), name='all_movies'),
    path('movie/<int:id>/', MovieView.as_view(), name='movie'),
    path('people/', PeopleView.as_view(), name='people'),
    path('person/<int:id>/', PersonView.as_view(), name='person'),
]
