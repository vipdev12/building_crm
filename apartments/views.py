from django.shortcuts import render
from rest_framework import viewsets, status, views, generics
from rest_framework.response import Response

from .models import Apartment
from .serializers import ApartmentSerializer


# Create your views here.

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response([serializer.data, {'message': 'Изменения сохранены'}],
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApartmentFilterView(generics.ListAPIView):
    serializer_class = ApartmentSerializer

    def get_queryset(self):
        apartment_status = self.kwargs.get('status')
        print(apartment_status)
        try:
            queryset = Apartment.objects.filter(status=apartment_status)
            return queryset
        except Apartment.DoesNotExist:
            return Apartment.objects.none()

