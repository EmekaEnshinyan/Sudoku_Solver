'''
a table of conetents for project, url declarations

path() args definition: 
 route - that contains the url pattern. they do not search GET and POST params, nor domain name
 view - when django find a matching pattern it calls the view funct with an httprequest
 kwargs - arbitrary keyword args that cna be passed to dict to target 
 name - allows you to refer to your url unambiguously form elsewhere in django (e.g. templates)
        allows global changes to url patterns

'''

"""
URL configuration for Sudoku_Solver project.

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
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    
]
