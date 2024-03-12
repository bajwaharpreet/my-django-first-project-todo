from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from guggu.models import contactus
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login



def home(request):

    # return HttpResponse("hellowhat are doing") 
    return render(request,"home.html")
def contactusx(request):
  
    return render(request,"contactus.html")

def aboutus(request):
  
    return render(request,"aboutus.html")

def services(request):
  
    return render(request,"services.html")

def servicesus(request):
#    ORM
   mydata=contactus.objects.all().order_by("-id")
#    print(mydata)
   context={"records":mydata}
   return render(request,"services.html",context)
   

def savethisdata(request):
  if request.method=="POST":
    fullname = request.POST.get("frame")
    emailaddress= request.POST.get("email")
    phonenumber = request.POST.get("number")
    massage = request.POST.get("massage")
    imx = request.FILES.get("imgg")


    mymassage=f"""
        this is user contact us formdata
        username: {fullname}
        useremail:{emailaddress}
        phonenumber:{phonenumber}
        massage:{massage}

        THANK YOU....)
        """
                     

    
        

    mail= EmailMessage("this email coming for django",mymassage,"bajwaharpreetkaur0225@gmail.com",["bajwaharpreetkaur0225@gmail.com","sweetpreet.kaur1@gmail.com"])

    mail.send()

    mydata=contactus (username=fullname, useremail= emailaddress,phonenumber=phonenumber,massage=massage, myimages = imx)

    messages.success(request,"Data saved successfully")



    mydata.save()
    return redirect("services")

    # return HttpResponse(f"data save succefully{frame},{email},{phonenumber},{massage}")

def deletethisdata(request,myid):
#    data=contactus.objects.all()
   data=contactus.objects.get(id=myid)

   messages.success(request,"Data delete successfully")

   data.delete()
#return HttpResponse(f"data deleted....{myid}")
   return redirect("services")


def updateharp(request,myid):
   
   data=contactus.objects.get(id=myid)
   return render(request,"updatedata.html",{"data" : data})
   
   
   
def udpdatetghiskagsdiayf(request, hey):
    if request.method=="POST":
        fullname = request.POST.get("frame")
        emailaddress= request.POST.get("email")
        phonenumber = request.POST.get("number")
        massage = request.POST.get("massage")

        mydata = contactus.objects.get(id = hey)

        mydata.username = fullname
        mydata.useremail = emailaddress
        mydata.phonenumber = phonenumber
        mydata.massage = massage

        mydata.save()

    return redirect("services")


def searchhing(request):
   
   mysearchelement = request.GET['q']

   data = contactus.objects.filter(username = mysearchelement) or contactus.objects.filter(phonenumber = mysearchelement)   
   return render(request, "services.html", {"records" : data})


def signup(request):
   
   if request.method == "POST":
      
      username = request.POST.get("Username")
      email = request.POST.get("email")
      password = request.POST.get("password")
      Fullname = request.POST.get("FullName")

      saveuser=User.objects.create_user(username=username,email=email,password=password,first_name=Fullname)

      messages.success(request,"user the data successfully!....")

      saveuser.save()

   return render(request,"signup.html")


def loginhere(request):
   if request.method=="POST":
      name=request.POST.get("username")
      passx=request.POST.get("password")

      usercheck= authenticate(username=name,password=passx)

      if usercheck is not None:
         login(request,usercheck)
         messages.success(request,"login successfully done")

      else: 
         
         messages.warning(request,"request please enter valid Crentationals!")

   
   return render(request,"login.html")

def logoutthere(request):
   
   logout(request)
   return render(request,"login.html")

 