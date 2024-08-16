from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hospitalapp.forms import usersignup
from hospitalapp.models import Login, doctoradd, schedule, book
from hospitalapp.serializer import doctoraddserializer, doctorsignupserializer, scheduleserializer, bookserializer


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
        print(view)
        v = book.objects.filter(schedule=view)
        print(v)
        if v.exists():
            print("exist")
            return Response(status=status.HTTP_208_ALREADY_REPORTED)
        else:
            if request.method == 'POST':
                print("post")
                serializer = bookserializer(data=request.data)
                print("hi")
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except:
        if request.method == 'GET':
            view = book.objects.all()
            serializer = bookserializer(view, many=True)
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def userscheduleget(request, pk):
    try:
        view = book.objects.get(user=pk)
        print(view)

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
