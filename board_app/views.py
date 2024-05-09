from rest_framework import generics
from .models import Board
from .serializers import BoardSerializer

class BoardListCreate(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

print("hello")
