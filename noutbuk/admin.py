from django.contrib import admin
from .models import Noutbuk


# Register your models here.

class SortNoutbuk(admin.ModelAdmin):
    list_filter = ['name_n', 'price_n']
    search_fields = ['name_n', 'price_n', 'make_n']


admin.site.register(Noutbuk, SortNoutbuk)
