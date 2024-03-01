from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from login.models import Useradd,Contact
from django.contrib.auth.decorators import login_required



url="https://www.bikewale.com/bajaj-bikes/"
resp=requests.get(url).content
soup=BeautifulSoup(resp,'html.parser')


links=soup.find_all("div",class_="imageWrapper")
pricess=soup.find_all("div",class_="text-bold")


bajlink=[]
prices=[]
title=[]    
images=[]


for k in links:
    k1=k.a.img["src"]
    i="https://www.bikewale.com/"+k.a["href"]
    p=k.a.img["title"]

    bajlink.append(i)

    images.append(k1)
    title.append(p)
for pr in pricess:
    p1=pr.text
    prices.append(p1)
    
mylist=zip(bajlink,
prices,
title,   
images
)


def bajaj(request):
    return render(request,"bajaj.html",{ 'mylist':mylist})




url0="https://www.zigwheels.com/upcoming-bikes"

resp0=requests.get(url0).content
soup9=BeautifulSoup(resp0,'html.parser')
aimg=[]
atit=[]
apri=[]
al=[]

links0=soup9.find_all("div",class_="clr mk-img-h")
links9=soup9.find_all("div",class_="clr-bl p-5")
lin=soup9.find_all("div",class_="p-15 pt-0 sl-mt20")

for n1 in lin:
    o7="https://www.zigwheels.com"+n1.a['href']
    al.append(o7)
for o in links0:
  
    o2=o.img['title']
    atit.append(o2)
    o1=o.img['src']  
    aimg.append(o1)
for m in links9:
    m1=m.text
    apri.append(m1)
mylist3=zip(aimg,
atit,
apri,al
)
@login_required(login_url='login')
def bike(request):
    return render(request,"base.html",{ 'mylist3':mylist3})

def contact(request):
    return render(request,"contact.html")
url1="https://autoportal.com/newbikes/heromotocorp/"

resp1=requests.get(url1).content
soup1=BeautifulSoup(resp1,'html.parser')

links1=soup1.find_all("div",class_="text-center")
links2=soup1.find_all("div",class_="models-list__body")
linksp=soup1.find_all("div",class_="models-list__price")
herolink=[]
heroname=[]
heroprices=[]


for e in links2:
    v="https://autoportal.com"+e.a["href"]

    b=e.a.text.strip()
    b1=b.replace("\n"," ")
    herolink.append(v)
    heroname.append(b1)



heroimag=[]
for l in links1:
    for l in links1:
        l1=l.span.img['data-original']
        if  l1.endswith(".jpeg"):
            l2=l1
            heroimag.append(l2)
        elif l1.endswith("png"):
            l3=l1[:-3]+'jpg'
            heroimag.append(l3)
        elif l1.endswith("jpg"):
            l3=l1
            heroimag.append(l3)
    


for w in linksp:
    w1=w.text.strip()
    heroprices.append(w1)
mylist1=zip(heroimag,heroprices,heroname,herolink)
    
def hero(request):

    return render(request,"hero.html",{ 'mylist1':mylist1})

url2="https://www.zigwheels.com/newbikes/Honda"

resp2=requests.get(url2).content
soup2=BeautifulSoup(resp2,'html.parser')
hondimg=[]
hondlink=[]
hondatitle=[]
hondapric=[]
links2=soup2.find_all('div',class_="clr mk-img-h")
links3=soup2.find_all('div',class_="p-15 mt-negative")
linkspri=soup2.find_all('div',class_="clr-bl p-5")
for t in links2:
    t1=t.img['src']
    
    hondimg.append(t1)

for e in links3:
    e1=e.a['href']
    e2=e.a['title']
    hondatitle.append(e2)
    hondlink.append(e1)
for d in linkspri:
    d1=d.text
    hondapric.append(d1)


mylist2=zip(hondimg,
hondlink,
hondatitle,
hondapric)

def honda(request):
    return render(request,"honda.html",{ 'mylist2':mylist2})
    


def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user= authenticate(username=username, password=password)
        if user is not None:

            login(request,user)
        
        return redirect("home")

    return render(request,"login.html")
def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        c = User.objects.create_user(username=username,email=email,password=password)
        c.save()
        return redirect("login")
    
    return render(request,"register.html")

def logout_user(request):
    logout(request)
    return redirect("login")




def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        


        c=Contact(name=name,email=email,message=message)
        c.save()
        return redirect("home")

    return render(request,"contact.html")

       

