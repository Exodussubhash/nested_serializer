from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from api_app.models import Member
from api_app.serializers import MemberSerializer
from django.views.decorators.csrf import csrf_exempt



class Members(APIView):
	def get(self,request):
		membe = Member.objects.all()
		serializer = MemberSerializer(membe,many=True)
		return Response(serializer.data)

def index(request):
	return render(request,'api_app/index.html')
