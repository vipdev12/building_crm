from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Manager
from .serializers import ManagerSerializer


# Create your views here.

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response([serializer.data, {'message': 'Менеджер добавлен'}],
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)