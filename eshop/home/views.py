from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from forex_python.converter import CurrencyRates
from .cuntry_currencies import CURRENCIES_BY_COUNTRY_CODE
from django.contrib.gis.geoip2 import GeoIP2
from ipware import get_client_ip
from .models import*
from .forms import*


# home view start
@login_required
def user_home(request):
    search_form = SearchForm()
    cardlen = 0
    try:
        card = UserCard.objects.get(user_id=request.user.id)
        cardlen = len(card.product.all())
    except:
        pass
    location = {}
    #receive usr location 
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        return render(request, 'errors.html')
    else:
        if is_routable:
            geoip2_obj = GeoIP2()
            location = geoip2_obj.country('client_ip')
        else:
            return render(request, 'errors.html')
    

    #static ip for test start
    '''geoip2_obj = GeoIP2()
    location = geoip2_obj.country('207.244.89.162')'''
    #static ip for testtest


    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            item = search_form.cleaned_data['search']
            products = Product.objects.filter(name__icontains=item)
            country_code = location['country_code']
            money_name = CURRENCIES_BY_COUNTRY_CODE[country_code][0]
            if country_code == 'BD':
                context = {
                    'products':products,
                    'search_form':search_form,
                    'cardlen':cardlen,
                }
                return render(request, 'index.html', context)
            else:
                for i in products:
                    i.price = i.price/84.8000
                if country_code == 'US':
                    context = {
                        'products':products,
                        'search_form':search_form,
                        'cardlen':cardlen,
                    }
                    return render(request, 'index.html', context)
                else:
                    currency_obj = CurrencyRates()
                    money = currency_obj.get_rate('USD', money_name)
                    for i in products:
                        i.price = i.price*money
                    context = {
                        'products':products,
                        'search_form':search_form,
                        'cardlen':cardlen,
                    }
                    return render(request, 'index.html', context)
    country_code = location['country_code']
    money_name = CURRENCIES_BY_COUNTRY_CODE[country_code][0]
    if country_code == 'BD':
        products = Product.objects.all()
        context = {
            'products':products,
            'search_form':search_form,
            'cardlen':cardlen,
        }
        return render(request, 'index.html', context)
    else:
        products = Product.objects.all()
        for i in products:
            i.price = i.price/84.8000
        if country_code == 'US':
            context = {
                'products':products,
                'search_form':search_form,
                'cardlen':cardlen,
            }
            return render(request, 'index.html', context)
        else:
            currency_obj = CurrencyRates()
            money = currency_obj.get_rate('USD', money_name)
            for i in products:
                i.price = i.price*money
            context = {
                'products':products,
                'search_form':search_form,
                'cardlen':cardlen,
            }
            return render(request, 'index.html', context)
#home view end


#add item in card
@login_required
def addcard(request, pk):
    user_id = request.user.id
    user = None
    try:
        user = UserCard.objects.get(user_id=user_id)
    except:
        pass
    if user:
        item = Product.objects.get(id=pk)
        user.product.add(item)
        return redirect('home-deshboard')
    else:
        user_card_obj = UserCard.objects.create(user_id=request.user)
        user_card_obj.save()
        user = UserCard.objects.get(user_id=user_id)
        item = Product.objects.get(id=pk)
        user.product.add(item)
        return redirect('home-deshboard')


#remove item in card
@login_required
def removecard(request, pk):
    user_id = request.user.id
    user = None
    try:
        user = UserCard.objects.get(user_id=user_id)
    except:
        pass
    if user:
        item = Product.objects.get(id=pk)
        user.product.remove(item)
        return redirect('home-deshboard')
    else:
        user_card_obj = UserCard.objects.create(user_id=request.user)
        user_card_obj.save()
        user = UserCard.objects.get(user_id=user_id)
        item = Product.objects.get(id=pk)
        user.product.remove(item)
        return redirect('home-deshboard')


#card list
@login_required
def card(request):
    card = UserCard.objects.get(user_id=request.user.id)
    location = {}
    #receive usr location 
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        return render(request, 'errors.html')
    else:
        if is_routable:
            geoip2_obj = GeoIP2()
            location = geoip2_obj.country('client_ip')
        else:
            return render(request, 'errors.html')


    #static ip for test start
    '''geoip2_obj = GeoIP2()
    location = geoip2_obj.country('207.244.89.162')'''
    #static ip for test


    country_code = location['country_code']
    money_name = CURRENCIES_BY_COUNTRY_CODE[country_code][0]
    if country_code == 'BD':
        products = card.product.all()
        context = {
            'products':products,
        }
        return render(request, 'cart.html', context)
    else:
        products = card.product.all()
        for i in products:
            i.price = i.price/84.8000
        if country_code == 'US':
            context = {
                'products':products,
            }
            return render(request, 'cart.html', context)
        else:
            currency_obj = CurrencyRates()
            money = currency_obj.get_rate('USD', money_name)
            for i in products:
                i.price = i.price*money
            context = {
                'products':products,
            }
            return render(request, 'cart.html', context)
            

#remove item insert card
@login_required
def card_item_remove(request, pk):
    user_id = request.user.id
    user = UserCard.objects.get(user_id=user_id)
    item = Product.objects.get(id=pk)
    user.product.remove(item)
    return redirect('card-list')