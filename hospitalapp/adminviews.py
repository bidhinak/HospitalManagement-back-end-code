from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hospitalapp.models import Notification, Login, doctoradd
from hospitalapp.serializer import Notificationserializer, doctorsignupserializer, doctoraddserializer


@api_view(['GET', 'POST'])
def Notificationdetails(request):
    if request.method == 'GET':

        view = Notification.objects.all()
        serializer = Notificationserializer(view, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = Notificationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def doctordetails(request):
    if request.method == 'GET':
        view = Login.objects.filter(is_doctor=True)
        serializer = doctorsignupserializer(view, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = doctorsignupserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def doctordetailsget(request, pk):
    try:
        view = Login.objects.get(pk=pk)
        print(view)

        v = doctoradd.objects.filter(details=view)
        print(v)
        if v.exists():
            print("exist")
            return Response(status=status.HTTP_208_ALREADY_REPORTED)
    except:
        if request.method == 'POST':
            serializer = doctoraddserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = doctorsignupserializer(view)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        view.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def admindoctoradd(request):
    if request.method == 'GET':
        view=doctoradd.objects.all()

        serializer = doctoraddserializer(view, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = doctoraddserializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
