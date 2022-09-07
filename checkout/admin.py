from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 'date', 'total',
    )

    fields = (
        'order_number', 'date', 'full_name',
        'email', 'street_1', 'street_2', 'county',
        'postcode', 'total',
    )

    list_display = (
        'order_number', 'date', 'full_name', 'total',
    )

    list_filter = ('date',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
