from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse, HttpResponse
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from hospitalapp.forms import doctorsignup
from hospitalapp.models import Login, schedule, book
from hospitalapp.serializer import scheduleserializer, bookserializer, usersignupserializer, doctorsignupserializer


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
        view = schedule.objects.all()
        serializer = scheduleserializer(view, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = scheduleserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def doctorscheduleget(request, pk):
    try:
        show = Login.objects.get(pk=pk)
        view = schedule.objects.filter(user=show)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = scheduleserializer(view, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def docscheduledelete(request, pk):
    try:
        view = schedule.objects.get(pk=pk)
        if request.method == 'DELETE':
            view.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def doctorschedulestatus(request, pk):
    try:
        show = book.objects.filter(schedule=pk)
        if request.method == "GET":
            serializer = bookserializer(show, many=True)
            return Response(serializer.data)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def doctorscheduleview(request, pk):
    try:
        show = Login.objects.get(pk=pk)
        if request.method == "GET":
            serializer = usersignupserializer(show)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def docaccountdelete(request, pk):
    try:
        show = Login.objects.get(pk=pk)
        print(show)
        if request.method == "DELETE":
            show.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def docprofileupdate(request, pk):
    try:
        view = Login.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = doctorsignupserializer(view)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = doctorsignupserializer(view, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def docChangePassword(request, pk):
    try:
        user = Login.objects.get(pk=pk)
    except Login.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    data = request.data

    old_password = data.get("old_password")
    if not check_password(old_password, user.password):
        return Response({"old_password": "Wrong password."}, status=status.HTTP_400_BAD_REQUEST)

    new_password = data.get("new_password")
    confirm_password = data.get("confirm_password")
    if new_password != confirm_password:
        return Response({"new_password": "New passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        validate_password(new_password, user)
    except Exception as e:
        return Response({"new_password": list(e)}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password)
    user.save()

    return Response({"detail": "Password changed successfully."}, status=status.HTTP_200_OK)
