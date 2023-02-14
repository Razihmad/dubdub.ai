from django.shortcuts import render
from datetime import datetime
from .models import Reminders
from .serializer import RemindersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class reminderAPI(APIView):
    def get(self,request,pk=None,format=None):
        if(pk is not None):
            rem = Reminders.objects.get(id=pk)
            serializer = RemindersSerializer(rem)
            return Response(serializer.data,status=status.HTTP_200_OK)
        reminders = Reminders.objects.all()
        serializer = RemindersSerializer(reminders,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,pk=None,format=None):
        dt = request.data.get("dateTime")
        cur = datetime.now()
        d = datetime.strptime(dt, "%d-%b-%Y-%H:%M:%S")
        if(d<=cur):
            res = {"msg":"Invalid datetime, As your date time has passed already"}
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
        deserializer = RemindersSerializer(data=request.data)
        if(deserializer.is_valid()):
            deserializer.save()
            res = {"msg":"Reminder Created Successfully"}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(deserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        id = request.data.get('id')
        if(Reminders.objects.filter(pk=id).exists()):
            reminder = Reminders.objects.get(pk=id)
            deserializer = RemindersSerializer(reminder,data=request.data,partial=True)
            if(deserializer.is_valid()):
                deserializer.save()
                res = {"msg":"Updated Successfully"}
                return Response(res,status=status.HTTP_200_OK)
            return Response(deserializer.errors,status=status.HTTP_400_BAD_REQUEST)
        res = {"msg":"No Such Id"}
        return Response(res,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None,format=None):
        try:
            rem = Reminders.objects.get(pk=pk)
            rem.delete()
            res = {"msg":"Deleted Successfully"}
            return Response(res,status=status.HTTP_200_OK)
        except:
            res = {"msg":"Id does not exist"}
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
        