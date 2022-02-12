from django.urls import path
from . import views

urlpatterns = [ #all possible access routes
    path("",views.index, name="index") # at path "/" run views.index
    #name optional used to identify url pattern (referencing)
    ,path("fart/", views.thomas,name="thomas"),
    path("y/",views.fartgobler,name="fart"),

    
    path('<str:name>',views.greet,name="greet") #this route can be any string
    #when this happens we call greet with this name argument as param
    # allows responsive  routes
]