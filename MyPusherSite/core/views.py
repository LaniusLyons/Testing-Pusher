# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

pusher = __import__('pusher')

def module_exists(module_name):
	try:
		__import__('pusher')
	except ImportError:
		return False
	else:
		return True

pusher_client = pusher.Pusher(
	app_id=settings.PUSHER_APP_ID,
	key=settings.PUSHER_KEY,
	secret=settings.PUSHER_SECRET,
	ssl=True
)

# Create your views here.

@login_required(login_url='/login/')
def index(request):
	#pusher = __import__('pusher')
	pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
	pusher_client.trigger(request.user.perfil.getChanelName(), 'check-code', {'message': 'Conectado'})
	return render(request,'index.html',{'key':settings.PUSHER_KEY})


def main(request):
	return render(request,'login.html',{})


def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/login/')


def login(request):
	if request.method == 'POST':
		email = request.POST.get('email',None)
		password = request.POST.get('password',None)
		message = None
		print email, password
		if email and password :
			user = authenticate(username=email, password=password)
			print user
			if user:
				if user.is_staff:
					return HttpResponseRedirect(reverse('admin:index'))

				auth_login(request, user)
				return HttpResponseRedirect(reverse('index'))

			else:
				message = 'Usuario Inválido'
		else:
			message = 'Error de parámetros'

		return render(request,'login.html',{'error':message})
	else:
		return render(request,'login.html')


@login_required(login_url='/login/')
def posting(request):
	print 'holi', request.POST.get('text',None)	
	pusher_client.trigger('private-'+request.user.perfil.getChanelName(), 'check-code', {'message':'CHECK CODE - POSTING'})
	return JsonResponse({'message':'CHECK CODE - POSTING'})



def auth_pusher(request):
	if request.user:
		if request.user.is_authenticated():
			channel = request.POST.get('channel_name',None)
			socket_id = request.POST.get('socket_id',None)
			if channel and socket_id:
				auth = pusher_client.authenticate(
					channel= channel,
					socket_id=socket_id
					)
				return HttpResponse(json.dumps(auth), content_type="application/json")
	return JsonResponse({'message':'No Authenticated'})

