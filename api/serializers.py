from rest_framework import serializers
from wallet.models import WalletUser, Account
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["bank_name", "account_name", "amount"]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["bank_name", "account_name", "amount"]


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']


class WalletUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
