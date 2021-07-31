from input.models import Login_form
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate 
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request,"index.html")
def registeruser(request):
    
    if request.method == "POST":
      username = request.POST.get("username",None)
      email = request.POST.get("email",None)
      password = request.POST.get("password",None)
      try:
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        Login_form( username= username, email=email, password= password ).save()
        
      except:
        messages.success(request, " Username already Taken! Try With another Username...")
        return render( request, "registeruser.html", {"username":username, "email":email})
      
      return redirect ("/makebot/make_bot")
      
    return render( request, "registeruser.html")


def login(request):
 if request.method=="POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
  
      user = authenticate(username=username, password=password)

      if user is not None:
        
        return redirect ("/makebot/make_bot")
               
      else:
        return redirect("/makebot/error/")
    
 return render( request, "login.html")
  


def logoutuser(request):
     logout(request)
     return render ( request, "logoutuser.html")


