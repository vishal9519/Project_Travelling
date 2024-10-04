from django.contrib import admin
from django.urls import path
from home import views
from .views import redirect_to_external_site
urlpatterns = [
    path("", views.index , name='home'),
    path("first",views.first,name='first'),
    path("jorhat",views.jorhat,name="jorhat"),
    path("manikar",views.manikar,name="manikar"),
    path("kasol",views.kasol,name="kasol"),
    path("jodhpur",views.jodhpur, name = "jodhpur"),
    path("varanasi",views.varanasi, name = "varanasi"),
    path("sikkim",views.sikkim, name = "sikkim"),
    path("tosh",views.tosh, name = "tosh"),
    path("spiti",views.spiti, name = "spiti"),

   path('redirect/', redirect_to_external_site, name='redirect_to_external_site'),
   path('mountain', views.mountain, name='mountain'),
   path('beach', views.beach, name='beach'),
   path('temple', views.temple, name='temple'),



    

    

    path("about", views.about , name='about'),
    path("acadmics", views.acadmics , name='acadmics'),
    path("contact", views.contact , name='contact'),
    
]
