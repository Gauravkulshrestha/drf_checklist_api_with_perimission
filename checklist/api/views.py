from urllib import request
from rest_framework import viewsets
from .models import Checklist, ChecklistItem
from .serializers import ChecklistSerializer, ChecklistItemSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsOwner
from rest_framework import status

class CheckListView(ListCreateAPIView):
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = Checklist.objects.filter(user=self.request.user)
        return queryset

class CheckListsView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = Checklist.objects.filter(user=self.request.user)
        return queryset

class CheckListItemCreateAPIView(CreateAPIView):
    serializer_class = ChecklistItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]

class CheckListItemAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChecklistItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = ChecklistItem.objects.filter(user=self.request.user)
        return queryset

class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            responce_data =  {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            }
        return Response(responce_data)

class LogOutAPIView(APIView):

    def post(self, request, format=None):        
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:                   
            return Response(status=status.HTTP_400_BAD_REQUEST)