from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class WalletUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=11)


class Account(models.Model):
    bank_name = models.CharField(max_length=235)
    account_number = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=9, decimal_places=2)


class Card(models.Model):
    card_number = models.CharField(max_length=16)
    card_name = models.CharField(max_length=255)
    cvv = models.CharField(max_length=3)
    expiry_date = models.DateField()


class Beneficiary(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()


class Wallet(models.Model):
    user = models.OneToOneField(WalletUser, on_delete=models.CASCADE, related_name='user')
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=models.CASCADE)
