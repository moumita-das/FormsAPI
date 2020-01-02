from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import  HttpResponse
from django.contrib import messages
from .forms import UserForm, ItemForm
from .models import ItemList
from django.http import JsonResponse

def create_view(request):
    if request.user.is_authenticated:
        form = ItemForm()
        if request.method == 'POST':
            form = ItemForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Form uploaded successfully')
                return render(request, 'index.html', {'form': ItemForm()})
            else:
                messages.error(request, 'Form not submitted')
                return render(request, 'index.html', {'form': form})
        return render(request, 'index.html', {'form': form})
    else:
        # User is not logged in
        auth_form = UserForm()
        return render(request,
                      'login.html',
                      {'auth_form': auth_form})

def retrieveView(request):
    model = ItemList.objects.all()
    item = model[::-1][0]
    data = {"results": {
        "first name": item.fname,
        "last name": item.lname,
        "DOB": item.dob,
        "img": item.img.path
    }}
    return JsonResponse(data)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                messages.warning(request, 'Logged in!')
                return redirect('/')
            else:
                messages.warning(request, 'Your account has been de-activated')
                auth_form = UserForm()
                return render(request,
                              'login.html',
                              {'auth_form': auth_form})

        else:
            messages.warning(request, 'Invalid credentials')
            auth_form = UserForm()
            return render(request,
                          'login.html',
                          {'auth_form': auth_form})

    else:
        return create_view(request)

def logout_view(request):
    logout(request)
    return redirect('/')

