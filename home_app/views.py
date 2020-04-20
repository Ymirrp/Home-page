from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import TopSites as TP
from .forms import AddSiteForm, RegisterUserForm
from .feeds import *
import requests


def index(req):
    if req.user.is_authenticated:
        return redirect('home')
    return redirect('login')


def reroute(req, url):
    link = TP.objects.get(url=url)
    link.clicks += 1
    link.save()
    return HttpResponseRedirect(url)


def user_login(req):
    print(req.POST)
    if req.method == 'POST':
        if '@' in req.POST['uname']:
            email = req.POST['uname']
            usern = User.objects.get(email=email).get_username()
        else:
            usern = req.POST['uname']
        passw = req.POST['pword']
        user = authenticate(req, username=usern, password=passw)
        if user is not None:
            login(req, user)
        return redirect('home')
    form = RegisterUserForm()
    return render(req, 'login.html', {'form': form})


def user_logout(req):
    logout(req)
    return redirect('index')


def user_reg(req):
    if req.method == 'POST':
        form = RegisterUserForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            pw = form.cleaned_data.get('password1')
            user = authenticate(req, username=username, password=pw)
            if user is not None:
                login(req, user)
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(req, 'register.html', {'form': form})


def home(req):
    if req.user.is_authenticated:
        user = req.user
        user_name = User.objects.get(username=user).first_name
        if user_name == '':
            user_name = user
        feeds = get_feed()
        all_sites = get_all_sites(user)
        cat_sites = get_listed_sites(all_sites)
        cats = get_categories(cat_sites)
        return render(req, 'home.html', {
            'sites': cat_sites,
            'categories': cats,
            'all_cats': TP.CATEGORIES,
            'feeds': feeds,
            'form': add_site(req),
            'user': user_name,
        })
    return redirect('index')


def get_all_sites(user):
    return list(TP.objects.filter(_user=user))


def get_listed_sites(sites_lst):
    d = {}
    for i in sites_lst:
        if i.categories not in d:
            d[i.categories] = []
        site_d = {
            "id": i.id,
            "name": i.name,
            "img": i.img,
            "url": i.url,
            # "order_no": i.order_no,
            "clicks": i.clicks,
            "category": i.categories
        }
        d[i.categories].append(site_d)
    return d


def get_categories(cat_sites):
    cats = []
    for cat in cat_sites:
        for s in cat_sites[cat]:
            if s['category'] not in cats:
                cats.append(s['category'])
    return cats


def add_site(req):
    if req.method == 'POST':
        form = AddSiteForm(data=req.POST)
        if form.is_valid():
            user = req.user
            name = req.POST['name']
            url = req.POST['url']
            img = req.POST['img']
            category = req.POST['categories']
            if name == '':
                name = url
            if img == '':
                img = "https://www.google.com/s2/favicons?domain="+url
            TP(_user=user, name=name, url=url, img=img, categories=category).save()
    else:
        return AddSiteForm()
    return redirect('home')


def edit_site(req, s_id):
    if req.method == 'POST' and req.user.is_authenticated:
        site = TP.objects.get(id=s_id)
    return redirect('home')


def del_site(req, s_id):
    if req.user.is_authenticated:
        TP.objects.get(id=s_id).delete()
        return HttpResponse("Site " + str(s_id) + " deleted")
    return HttpResponse("Error: User not logged in!")
    # return redirect('home')


def get_weather_view(req):
    lat = req.GET.get('lat')
    lon = req.GET.get('lon')
    res = get_weather(lat, lon)
    return JsonResponse(res)


def unavailable(req):
    return render(req, 'unavailable.html')
