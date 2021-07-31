
from django.http import response
from django.shortcuts import redirect, render,loader

import os
from django.contrib.auth import logout, authenticate , login
from django.contrib.auth.models import User

# Create your views here.
from makebot import models
from makebot.models import profile

from input.models import Login_form
def make_bot(request):
    

    
    
    return render(request,"make_bot.html")

def info(request):
    
    
    if request.method=="POST":
        
        
        name=request.POST.get("name",None)
        email=request.POST.get("email",None)
        school=request.POST.get("school",None)
        
        skill=request.POST.get("skill",None)
        previous_work=request.POST.get("previous_work",None)
        acherviment=request.POST.get("acherviment",None)
        acherviment1=request.POST.get("acherviment1",None)
        about=request.POST.get("about",None)
        web=request.POST.get("web",None)
        number=request.POST.get("number",None)
        high=request.POST.get("high",None)
        sec=request.POST.get("sec",None)
        branch=request.POST.get("branch",None)
        CGPA=request.POST.get("CGPA",None)
        link=request.POST.get("link",None)
        coding=request.POST.get("coding",None)
        #img=request.POST.get("img",None)
        

        profile(name= name, email=email, school= school, skill=skill , about=about,acherviment=acherviment,acherviment1=acherviment1,web=web,number=number,previous_work=previous_work,branch=branch,CGPA=CGPA,high=high,sec=sec,link=link,coding=coding).save()
        
    
        return redirect("/makebot/list/")
        
    return render(request,"info.html")
def resume(request,id):

    user_profile=profile.objects.get(pk=id)
    '''template= loader.get_template("resume.html")
    html=template.render({'i':user_profile})
    option={
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf=pdfkit.from_string(html,False,option)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachments'
    return response'''
    

    return render(request,"resume.html",{'i':user_profile})
def list(request):
    Profile=profile.objects.all()
    return render(request,"list.html",{'x':Profile})

'''def pas(request):
    if request.method =="POST":
        Login_form.objects.all()
        password=request.POST.get("password")
        user = User.objects.create_user(password=password)
        user.save()
        user = authenticate( password=password)
        return render(request,"pas.html")

    return render(request,"pass.html")'''
    
    