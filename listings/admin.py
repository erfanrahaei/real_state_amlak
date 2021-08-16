from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    List_display=('id','title','is_published','price','list_date','realtor')
    List_display_links=('id','title')
    List_filter=('realtor',)
    List_editable=('is_published',)
    search_fields=('title','description','address','city','state','zipcode','price')
    list_per_page=25

admin.site.register(Listing,ListingAdmin)     