import pusher
from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.conf import settings


# pusher_client = pusher.Pusher(
# 	app_id=settings.PUSHER_APP_ID,
# 	key=settings.PUSHER_KEY,
# 	secret=settings.PUSHER_SECRET,
# 	ssl=True
# )	
# pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
# Create your views here.

def index(request):
	return render(request,'index.html',{'key':settings.PUSHER_KEY})
