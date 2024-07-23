from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hospitalapp.forms import doctorsignup
from hospitalapp.models import schedule
from hospitalapp.serializer import scheduleserializer


@csrf_exempt
def doctor_signup(request):
    result_data = None
    if request.method == 'POST':
        form = doctorsignup(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.is_active = True
            form.is_doctor = True
            form.save()
            result_data = True
    try:
        if result_data:
            data = {'result': True}
        else:
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



@api_view(['GET', 'POST'])
def doctorscheduleadd(request):
    if request.method == 'GET':
        u = request.user
        print(u)
        view = schedule.objects.all()
        serializer = scheduleserializer(view, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = scheduleserializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Hello, {request.user.username}")
    else:
        return HttpResponse("You are not logged in")
