from django.core import serializers
from rest_framework import status, generics
from rest_framework.response import Response
from .serializer import EmployeeSerializer, UpdateEmployeeSerializer
from rest_framework.views import APIView
import json
from .models import Employee


class EmployeeAll(APIView):
    @staticmethod
    def get(request):
        try:
            return Response(list(map(lambda x: x['fields'], tuple(json.loads(serializers.serialize("json", Employee.objects.all()))))), status=status.HTTP_200_OK)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeProcess(generics.GenericAPIView):
    @staticmethod
    def post(request, *args, **kwargs):
        try:
            serializer = EmployeeSerializer(data=json.loads(request.body))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)


class EmployeeUpdate(generics.GenericAPIView):
    try:
        @staticmethod
        def put(request):
            try:
                serializer = UpdateEmployeeSerializer(Employee.objects.get(id=request.GET.getlist('pk')[0]), data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)

        @staticmethod
        def delete(request):
            try:
                Employee.objects.get(id=request.GET.getlist('pk')[0]).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                print(e)
                return Response('doesnot exist with pk', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        print('here in exception')
        print(e)

