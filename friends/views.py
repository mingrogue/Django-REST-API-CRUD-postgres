from django.core import serializers
from django.views import View
from rest_framework import status, generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializer import FriendsSerializer
from rest_framework.views import APIView
import json
from .models import Friends
from django.views import View

class FriendsView(APIView):
    def get(self, request):
        try:
            return Response(list(map(lambda x: x['fields'], tuple(json.loads(serializers.serialize("json", Friends.objects.all()))))), status=status.HTTP_200_OK)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


class FriendsAdd(generics.GenericAPIView, mixins.CreateModelMixin):
    def post(self, request, *args, **kwargs):
        try:
            serializer = FriendsSerializer(data=json.loads(request.body))
            if serializer.is_valid():
                #data = serializer.validated_data
                #print(data)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
