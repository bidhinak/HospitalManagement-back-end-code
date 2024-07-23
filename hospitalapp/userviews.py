from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hospitalapp.forms import usersignup
from hospitalapp.models import Login, doctoradd
from hospitalapp.serializer import doctoraddserializer


@csrf_exempt
def user_signup(request):
    result_data = None
    if request.method == 'POST':
        form = usersignup(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_active = True
            f.is_user = True
            f.save()
            result_data = True
    try:
        if result_data:
            data = {'result': True}
        else:
            print(list(form.errors))
            error_data = form.errors
            error_dict = {}
            for i in list(form.errors):
                error_dict[i] = error_data[i][0]
                data = {
                    'result': False,
                    'errors': error_dict
                }
    except:
        data = {
            'result': False
        }
    return JsonResponse(data, safe=False)


def home(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Hello, {request.user.username}")
    else:
        return HttpResponse("You are not logged in")

