from rest_framework import generics
from .models import Board
from .serializers import BoardSerializer
import os
import sys
import urllib.request
import urllib.parse
import urllib.request
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


class GetNewsView(APIView):
    def get(self, request, *args, **kwargs):
        encText = urllib.parse.quote("갈등")
        url = "https://openapi.naver.com/v1/search/news?query=" + encText
        client_id = settings.NAVER_CLIENT_ID
        client_secret = settings.NAVER_CLIENT_SECRET

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        
        try:
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if rescode == 200:
                response_body = response.read()
                data = json.loads(response_body.decode('utf-8'))  # JSON 데이터를 디코딩
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"error": f"Error Code: {rescode}"}, status=rescode)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BoardListCreate(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

print("hello")
