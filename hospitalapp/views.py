from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def doctor_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password1')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
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
    password = request.POST.get('password1')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.is_user:
            user_type = 'user'
        else:
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
    return JsonResponse(data, safe=False)


