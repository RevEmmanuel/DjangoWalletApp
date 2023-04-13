from rest_framework.viewsets import ModelViewSet
from wallet.models import WalletUser, Account
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .pagination import DefaultPageNumberPagination
from .serializers import AccountSerializer, CreateAccountSerializer, UserCreateSerializer, WalletUserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPageNumberPagination
    queryset = WalletUser.objects.all()
    serializer_class = WalletUserSerializer


class AccountViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CreateAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = WalletUser.objects.all()
    serializer_class = UserCreateSerializer


@api_view()
def user_detail(request, pk):
    user = get_object_or_404(WalletUser, pk=pk)
    serializer = WalletUserSerializer(user)
    return Response(serializer.data)

