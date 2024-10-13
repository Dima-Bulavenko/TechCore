from django.contrib import admin

from checkout import models


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'address_line_1',
        'address_line_2',
        'city',
        'county',
        'country',
        'postal_code',
        'last_update',
    ]
