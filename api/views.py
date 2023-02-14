from django.shortcuts import render
from datetime import datetime
from .models import Reminders
from .serializer import RemindersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# this is when user need only those work that are incomplete yet
class IncompleteReminder(APIView):
    def get(self,request,pk=None,format=None):
        if(pk is not None):
            if(Reminders.objects.filter(pk=pk).exists()):
                rem = Reminders.objects.get(pk=pk,status="Incomplete")
                serializer = RemindersSerializer(rem)
                return Response(serializer.data,status=status.HTTP_200_OK)
            res = {"msg":"No such data exists"}
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
        rem = Reminders.objects.filter(status="Incomplete")
        serializer = RemindersSerializer(rem,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
# this is when user need only those work that have been completed 
class CompleteReminder(APIView):
    def get(self,request,pk=None,format=None):
        if(pk is not None):
            if(Reminders.objects.filter(pk=pk).exists()):
                rem = Reminders.objects.get(pk=pk,status="Complete")
                serializer = RemindersSerializer(rem)
                return Response(serializer.data,status=status.HTTP_200_OK)
            res = {"msg":"No such data exists"}
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
        rem = Reminders.objects.filter(status="Complete")
        serializer = RemindersSerializer(rem,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

# for posting the reminders
class PostReminder(APIView):
    def post(self,request,format=None):
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

# to delete a particular reminder
class DeleteReminder(APIView):
    def delete(self,request,pk=None,format=None):
        try:
            rem = Reminders.objects.get(pk=pk)
            rem.delete()
            res = {"msg":"Deleted Successfully"}
            return Response(res,status=status.HTTP_200_OK)
        except:
            res = {"msg":"Id does not exist"}
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
        
# to update one of the reminder
class UpdateReminder(APIView):
    def put(self,request,pk=None,format=None):
        if(Reminders.objects.filter(pk=pk).exists()):
            reminder = Reminders.objects.get(pk=pk)
            deserializer = RemindersSerializer(reminder,data=request.data,partial=True)
            if(deserializer.is_valid()):
                deserializer.save()
                res = {"msg":"Updated Successfully"}
                return Response(res,status=status.HTTP_200_OK)
            return Response(deserializer.errors,status=status.HTTP_400_BAD_REQUEST)
        res = {"msg":"No Such Id"}
        return Response(res,status=status.HTTP_400_BAD_REQUEST)