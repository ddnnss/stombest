from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import *


@admin.register(User)
class UserAdmin(DjangoUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (_('Данные пользователя'), {'fields': ('name','surname',  'phone', )}),
        (_('Даты регистрации и последнего посещения'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone'),
        }),
    )
    list_display = ('email', 'name','surname', 'phone')

    ordering = ('email',)
    search_fields = ('email', 'name','surname', 'phone')

