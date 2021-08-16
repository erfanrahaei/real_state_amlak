import listings
from django.core import paginator
from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import price_choices,bedroom_choices,state_choices

from .models import Listing


def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings,5)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings':paged_listings
    }
    return render(request,'listings/listings.html',context)


def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)    
    context={
        'listing':listing
    }
    return render(request,'lisitngs/listings.html',context)

def search(request):
    queryset_list=Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)

    #city
    if 'city'in request.GET:
        city=request.Get['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city) 

    #state
    if 'state'in request.GET:
        state=request.Get['state']
        if state:
            queryset_list=queryset_list.filter(state__iexact=state) 

    #bedrooms
    if 'bedrooms'in request.GET:
        bedrooms=request.Get['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)                     
            
   
    #price
    if 'price'in request.GET:
        price=request.Get['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)


    context={
        'state_choices':state_choices,
        'bedroom_choces':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'values':request.GET
    }        

    return render(request,'lisitngs/search.html',context)