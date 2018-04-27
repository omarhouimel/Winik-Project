from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.Serializer import ContactSerializer
from home.forms import SingupForm
from home.models import GaleriePhoto, Contact, Position


def index(request):
   image=GaleriePhoto.objects.all()


   return render(request,'home/index.html',locals())



def login(request):
   return  render(request, 'login/login.html')


def singup(request):

   form=SingupForm(request.POST or None)
   contact = Contact()

   if request.method=='POST':
      if form.is_valid():

         contact.full_name = form.cleaned_data['full_name']
         contact.password=form.cleaned_data['password']
         contact.user_name=form.cleaned_data['user_name']
         contact.email=form.cleaned_data['email']
         contact.save()
      else:
         print(form.errors)
         # redirect(index)







   return  render(request,'Singup/singup.html',{'form':form})


def map(request):
   position=Position.objects.all()
   lat=35.8245029
   lng=10.634584000000018
   return render(request,'Map/map.html',locals())

@api_view(['GET', 'POST'])
def contactlist( request):

    if request.method=='GET':
        contact=Contact.objects.all()
        serializer=ContactSerializer(contact,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
       print(request)
       lng = float(request.POST.get("lng"))
       lat=float(request.POST.get("lat"))
       place= (request.POST.get("place"))
       position=Position()
       position.lat=lat
       position.lng = lng
       position.place=place
       position.save()


    pass