import rest_framework.generics
from rest_framework import generics, permissions
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer


# Create your views here.
class MenuItemsView(rest_framework.generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingsView(rest_framework.generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# class BookingView(APIView):
#
#     def get(self, request, pk):
#         items = Booking.objects.get(pk=pk)
#         serializer = BookingSerializer(items)
#         return Response(serializer.data)

@permission_classes([IsAuthenticated])
class MenuView(APIView):

    def get(self, request):
        items = Menu.objects.all()
        serializer_class = MenuSerializer(items, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})

    # def delete(self, request, *pk):
    #     items = Menu.objects.get(pk=pk)
    #     serializer = MenuSerializer(items)
    #
    #     if serializer:
    #         items.delete()
    #         return Response({'status': 'success', 'data': serializer.data})



class SingleMenuView(APIView):

    def get(self, request, pk):
        items = Menu.objects.get(pk=pk)
        serializer = MenuSerializer(items)
        return Response(serializer.data)

    def delete(self, request, pk):
        items = Menu.objects.get(pk=pk)

        if items:
            items.delete()
        return Response(status.HTTP_200_OK)

    def patch(self, request, pk):
        items = Menu.objects.get(pk=pk)

        if items:
            items.update()
            serializer = MenuSerializer(items)
            return Response(serializer.data)
        return Response(status.HTTP_200_OK)




@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def secured_view(request):
        return Response({'message': 'need authentication'})


class BookingViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



def index(request):
    return render(request, 'index.html', {})



