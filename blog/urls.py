from django.urls import path
from . import views
#Hier importieren wir die Django-Funktion path und alle unsere views aus unserer blog-Applikation

urlpatterns=[
    path("",views.post_list, name="post_list"),
]