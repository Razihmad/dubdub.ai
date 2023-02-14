from django.shortcuts import render
from datetime import datetime
from .models import Reminders
from .serializer import RemindersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class reminderAPI(APIView):
    def get(self,request,pk=None,format=None):
        reminders = Reminders.objects.all()
        serializer = RemindersSerializer(reminders,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,pk=None,format=None):
        dt = request.data.get("dateTime")
        cur = datetime.now()
        d = datetime.strptime(dt, "%d-%b-%Y-%H:%M:%S")
        if(d<=cur):
            res = {"msg":"Invalid datetime, As you date time has passed already"}
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
        deserializer = RemindersSerializer(data=request.data)
        if(deserializer.is_valid()):
            deserializer.save()
            res = {"msg":"Reminder Created Successfully"}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(deserializer.errors,status=status.HTTP_400_BAD_REQUEST)