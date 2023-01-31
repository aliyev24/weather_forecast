import requests
from . import models
from . import forms
from . import services
from django.shortcuts import render, redirect

from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3473651768de5e545f7d20a5187dc1fd'
    forecast_data = []
    cities = models.Region.objects.all().order_by('-id')[:5]
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        forecast_data.append(weather)
    context = {'forecast_data': forecast_data}
    return render(request, 'core/index.html', context)

def user(request):
    form = forms.RegionForm()
    if request.method == 'POST':  # only true if form is submitted
        form = forms.RegionForm(request.POST)  # add actual request data to form for processing
        if form.is_valid():
            form = form.save(commit=False)
            if request.user.is_authenticated:
                form.user = request.user
                form.save()
                return redirect('user')

    if request.user.is_authenticated:
        user_city = models.Region.objects.filter(user=request.user)
        forecast_data = services.get_forecast(user_city)
        context = { 'forecast_for_user': forecast_data,'form': form}
        return render(request, 'core/user.html', context)
    else:
        return redirect('login')

class RegisterUser(CreateView):
    form_class = forms.Registration
    template_name = "core/registration.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'core/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_me(request):
    logout(request)
    return redirect('home')
