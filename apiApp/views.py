from django.shortcuts import render, HttpResponse
from .models import  Profile
from .serializer import ProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def postData(request, bio, name, phone_number):
    data = Profile(bio=bio, name=name, phone_number=phone_number)
    data.save()
    return HttpResponse("Successfully sent")
       
class ProfileList(APIView):
    def get(self, request, format=None):
        all_prof = Profile.objects.all()
        serializers = ProfileSerializer(all_prof, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)