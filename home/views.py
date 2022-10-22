from audioop import reverse
from distutils.command.upload import upload
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.urls import path, reverse_lazy
from django.http import Http404, HttpResponse
from home.forms import users_input
from .models import events_info, takePart
from django.contrib.auth.models import User, AnonymousUser
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import contactus, updateProfile, users_input, takePartF
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib import admin as adminn

# Create your views here.
from urllib.parse import (
    urlencode,
    ParseResult,
    SplitResult,
    _coerce_args,
    _splitnetloc,
    _splitparams,
    scheme_chars,
)
from huda.settings import GOOGLE_RECAPTCHA_SECRET_KEY
from json import loads
from urllib.request import (
    Request,
    urlopen,

)

from qrcode import *

from django.conf import settings

# from verify_email.email_handler import send_verification_email



def home_page(request):
    return render(request, "home_page.html")

def takePart(request):
    form = takePartF()
    if request.method == 'POST':
        form = takePartF(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "takePart.html", {'form': form})


def contactUs(request):
    form = contactus()
    if request.method == 'POST':
        form = contactus(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "contactUs.html", {'form': form})


def shows(request):
    events = events_info.objects.all()


    eventlist = []
    for event in events:
        eventlist.append({'event': event})

    context = {'event': eventlist}

    return render(request, "showsPage.html", context)


# def signin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             user = auth_login(request, username)
#             if user is not None:
#                 return redirect(home_page)
#                 print('he')
#             else:
#                 return redirect(signin)
#         except Exception as id:
#             print(id)
#     return render(request, "signIn.html")


# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         phone = request.POST['phone']

#         new_user = users_info(username=username, email=email, password=password,
#                               firstname=firstname, lastname=lastname, phone=phone)
#         new_user.save()
#         login(request, new_user)
#         return redirect(signin)
#     return render(request, "signUp.html")
img_name=''
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = users_input()
        if request.method == 'POST':
            # return render(request, 'signUp.html', {'img_name': img_name})
            form = users_input(request.POST)
            if form.is_valid():
                # inactive_user = send_verification_email(request, form)
                data = request.POST['first_name'] +" "+ request.POST['last_name']
                img = make(data)
                img_name = str(request.POST['username']) + '.png'

                img.save(settings.MEDIA_ROOT + '/' + img_name)

                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                data = urlencode(values).encode()
                req = Request(url, data=data)
                response = urlopen(req)
                result = loads(response.read().decode())
                if result['success']:
                    user = form.save()
                    auth_login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        return render(request, 'signUp.html', {'form': form})



def confirm(request):
    img_name = str(request.user.username) + '.png'

    return render(request, "confirmattending.html", {'img_name': img_name})


class UserUpdateView(UpdateView):
    model = User

    template_name: 'profile.html'

    form_class = updateProfile
    success_url: reverse_lazy('profile/')

    def get_object(self):
        return self.request.user
