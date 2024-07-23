from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def doctor_login(request):
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password1')
    print(password)
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        print("testing")
        print(request.user)
        if user.is_staff:
            user_type = 'admin'
        elif user.is_doctor:
            user_type = 'doctor'
        else:
            user_type = 'unknown'
        data = {
            'status': True,
            'result': {
                'id': user.id,
                'name': user.username,
                'email': user.email,
                'mobile': user.mobile,
                'department': user.department,
                'qualification': user.qualification,
                'photo': user.photo.url,
                'type': user_type
            }
        }
    else:
        data = {
            'status': False,
            'result': 'Invalid username or Password'
        }
    return JsonResponse(data, safe=False)


@csrf_exempt
def user_login(request):
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password1')
    print(password)
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        print(user)
        login(request, user)
        if user.is_user:
            print("ok")
            user_type = 'user'
        else:
            print("ok")
            user_type = 'unknown'
        data = {
            'status': True,
            'result': {
                'id': user.id,
                'name': user.username,
                'email': user.email,
                'mobile': user.mobile,
                'type': user_type
            }
        }
    else:
        data = {
            'status': False,
            'result': 'Invalid Username or Password'
        }
    print(data)
    print(request.user)
    return JsonResponse(data, safe=False)

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

@csrf_exempt
def new(request):
    print(request.user)
    return render(request,'new.html')
