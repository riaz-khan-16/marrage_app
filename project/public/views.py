from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from public.models import Intro
from public.serializers import IntroSerializer
import requests
from django.http import JsonResponse


@api_view(['GET', 'POST'])
def intro_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        intros = Intro.objects.all()
        serializer = IntroSerializer(intros, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IntroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def intro_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        intros = Intro.objects.get(pk=pk)
    except Intro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IntroSerializer(intros)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IntroSerializer(intros, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        intros.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


from django.http import HttpResponse
from django.template import loader
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import render,redirect



def regi(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        print(username,password,email)
        my_user=User.objects.create_user(username,email,password)
        my_user.save()
        print('Data Saved Successfully')
        return redirect('success')

    return  render(request,"regi.html")

def success(request):
    return render(request,'successfull.html')

from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        my_user=authenticate(request,username=username,password=password)

       
      
        if my_user is not None:
              login(request,my_user)
              return redirect('public')
              
        
        else:
            print('credential is wrong')

    return  render(request,"login.html")

def  logout1(request):
    logout(request)
    return render(request,"login.html")


def detail_regi(request):
    
    if request.method == 'POST':

        data = {
            'gender': request.POST['gender'],
            'mstatus': request.POST['mstatus'],
            'name': request.POST['name'],
            'age': request.POST['age'],
            'hometown': request.POST['hometown'],
            'present_address': request.POST['present_address'],
            'occupation': request.POST['occupation'],
            'height': request.POST['height'],
            'color': request.POST['color'],
            'blood': request.POST['blood'],

            # Add other fields as needed
        }


        print(request.POST['name'], request.POST['hometown'],request.POST['gender'],request.POST['mstatus'])
       
        # Make a POST request to the API endpoint
        response = requests.post('http://127.0.0.1:8000/persons/', data=data)

        # Handle the API response
        if response.status_code == 201:  # 201 means created
            return  render(request,"home.html")
        else:
            return JsonResponse({'error': 'Failed to create item'}, status=500)
        
    return  render(request,"detail_regi.html")
#fields = ['id', 'gender', 'mstatus', 'name', 'age', 'hometown','present_address','occupation','height','color','blood']


def dashboard(request):



    response = requests.get('http://127.0.0.1:8000/persons/')
    items=response.json()
   
    

    return  render(request,"home.html",{'items': items})


@login_required(login_url="/login/")
def public(request):

    response = requests.get('http://127.0.0.1:8000/persons/')
    items=response.json()
    
    

    return  render(request,"public.html",{'items': items})





