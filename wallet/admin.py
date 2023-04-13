from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import WalletUser, Account

# Register your models here.
# admin.site.register(WalletUser)
# admin.site.register(Account)
# admin.site.register(Transaction)


@admin.register(WalletUser)
class User(UserAdmin):
    pass


# @admin.register(WalletUser)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['title', 'isbn', 'genre', 'language', 'price']
#     list_editable = ['price']
#     list_per_page = 10


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'account_number', 'amount']
    list_per_page = 10
