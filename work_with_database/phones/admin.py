from django.contrib import admin

from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Phone, PhoneAdmin)
