from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hospitalapp.forms import usersignup
from hospitalapp.models import Login, doctoradd, schedule, book
from hospitalapp.serializer import doctoraddserializer, doctorsignupserializer, scheduleserializer, bookserializer, \
    usersignupserializer


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


@api_view(['GET', 'PUT', 'DELETE'])
def userdoctorprofileget(request, pk):
    try:
        show = doctoradd.objects.get(pk=pk)

        if request.method == 'GET':
            serializer = doctoraddserializer(show)
            return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def userbook(request, pk):
    try:
        view = schedule.objects.get(pk=pk)
        v = book.objects.filter(schedule=view)
        if v.exists():
            return Response(status=status.HTTP_208_ALREADY_REPORTED)
        else:
            if request.method == 'POST':
                serializer = bookserializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except:
        if request.method == 'GET':
            view = book.objects.all()
            serializer = bookserializer(view, many=True)
            return Response(serializer.data)


@api_view(['GET', ])
def userbookget(request):
    if request.method == 'GET':
        view = book.objects.all()
        serializer = bookserializer(view, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def userscheduleget(request, pk):
    try:
        view = book.objects.get(user=pk)
        if request.method == 'GET':
            serializer = scheduleserializer(view, many=True)
            return Response(serializer.data)

    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def usersearch(request):
    query = request.GET.get('q')
    if query:
        results = doctoradd.objects.filter(
            Q(name__icontains=query) | Q(department__icontains=query)
        )
    serializer = doctoraddserializer(results, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'DELETE'])
def useraccountdelete(request, pk):
    try:
        show = Login.objects.get(pk=pk)
        if request.method == "DELETE":
            show.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def userschedulestatus(request, pk):
    try:
        show = book.objects.filter(user=pk)
        if request.method == "GET":
            serializer = bookserializer(show, many=True)
            return Response(serializer.data)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def userscheduleview(request, pk):
    try:
        show = schedule.objects.get(pk=pk)
        if request.method == "GET":
            serializer = scheduleserializer(show)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def userChangePassword(request, pk):
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


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def userprofileupdate(request, pk):
    try:
        view = Login.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = usersignupserializer(view)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = usersignupserializer(view, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
