from django.shortcuts import render, redirect
from .models import List
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ListSerializer 


# Create your views here.
# def index(request):
#     if request.user.is_authenticated:

#         tasks = List.objects.all()
#         if request.method == "POST":
#             # task = request.POST.get('task')
#             # lists = List(task=task)
#             # if task:
#             #     lists.save()
#             #     return redirect('index')
#             task = request.POST.get('task')
#             if task:
#                 lists = List(task=task)
#                 lists.user = request.user
#                 lists.save()
#                 return redirect('index')
#             else:
#                 messages.error(request, 'An error occured')
#     else:
#         return redirect('login')
    
#     context = {'tasks': tasks}
#     return render(request, 'index.html', context)

# @login_required
# def update(request, pk):
#     task = List.objects.get(id=pk)
#     if request.method == 'POST':
#         update_task = request.POST.get('update')
#         if update_task:
#             task.task = update_task
#             task.save()
#             return redirect('index')
    
#     context = {'task': task}
#     return render(request, 'update.html', context)

# @login_required
# def delete(request, pk):
#     task = List.objects.get(id=pk)
#     if request.method == "POST":
#         task.delete()
#         return redirect('index')

#     context = {'task': task}
#     return render(request, 'delete.html', context)

# def signup_page(request):
    
#     if request.method == "POST":
#         username = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'This username already exist')
#         else:
#             user = User.objects.create_user(username=username, email=email, password=password)
#             user.save()
#             messages.success(request, 'User was created successfully')
#             user = authenticate(request, username=username, email=email, password=password)
#             login(request, user)
#             return redirect('index')
#             # return redirect('index')
        
#     context = {}
#     return render(request, 'signup.html', context)


# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']

#         user = authenticate(request, username=username, email=email, password=password) 
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             messages.error(request, "Don't have an account? Sign up")
#     return render(request, 'login.html')

# def logout_page(request):
#     logout(request)
#     return redirect('login')

# def logout_option(request):
#     return render(request, 'logout.html')



@api_view(['GET'])
def TaskApi(request):
    get_posts = List.objects.all()
    serializer = ListSerializer(get_posts, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def CreateTask(request):
    data = request.data
    serializer = ListSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The Post was successfully created"})
    else:
        return Response(serializer.errors, status=400)