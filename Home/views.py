from django.shortcuts import render, redirect
from .models import Booth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login
def home(request):
    booths=Booth.objects.all()
    context={
'booths':booths
    }
    return render(request,'Home/home.html',context)

def booth_details(request):
    if request.method == 'POST':
        id = request.POST.get('booth')
        booths=Booth.objects.get(id=id)
        context={
        'booths':booths
    }
        return render(request,'Home/Booth.html',context)
    return redirect('both_list')

def booth_list(request):
    booths=Booth.objects.all()
    if request.method == 'POST':
        booth_details(request)
    context={
        'booths':booths
    }
    return render(request,'Home/select_booth.html',context)
def login_Password(request):
    if request.method =='POST':
        password=request.POST.get('password')
        users=User.objects.all()
        for user in users:
            print(password, user.password)
            if check_password(password, user.password):
                login(request, user)
                return redirect('both_list')
            else:
                print("password not matched!")
    return render(request,'Home/password.html')
    

@csrf_exempt
def change_status(request):
    if request.method=="POST":
        id = request.POST['id']
        status = request.POST['status']
        booth=Booth.objects.get(id=id)
        booth.status=status
        booth.save()
        return JsonResponse({'status':'updated successfully!','booth':booth.status})
    return redirect('change_status')