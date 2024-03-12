from django.urls import path 
from guggu import views

urlpatterns = [path("home",views.home,name ="home"),
               path("contactus",views.contactusx,name ="contactus"),
 
               path("aboutus",views.aboutus,name ="aboutus"),
               path("services",views.servicesus,name ="services"),
               path("save-my-data",views.savethisdata),

               path("delete-record/<int:myid>",views.deletethisdata),

               
               path("update",views.updateharp,name="update"),
               
               path("update/<int:myid>",views.updateharp),

               path("updatethisdata/<int:hey>", views.udpdatetghiskagsdiayf),

               path("serch-my-data", views.searchhing),

               path("signup", views.signup,name="signup"),

               path("login", views.loginhere, name="login"),

               path("logout", views.logoutthere,name="logout"),

]







    


   
