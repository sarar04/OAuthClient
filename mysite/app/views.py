# Create your views here.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
import os,requests

from requests_oauthlib import OAuth2Session, OAuth2

from forms import loginform
import oauth_settings

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

def index(request):
	print 'debug: enter index' 
	return render(request,'app/index_t.html',{'form':loginform})

#Django authorization
def mylogin(request):
	
	#login authorization
	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password) 
		
		if user is not None:
			if user.is_active:

				login(request,user)
				userinfo = {'username':username}
				return render(request,'app/welcome_t.html',{'userinfo':userinfo})
			else:

				reason = username +' is not an active account.'
				return render(request,'app/welcome_t.html',{'reason':reason})
		else:
			reason = 'Alert !!! please enter right username and password'
			return render(request,'app/welcome_t.html',{'reason':reason})	
	else:
		raise render(request,'app/index_t.html',{'form':loginform})

	
def get_oauth_code(request):		
	print 'get the authorization web name and the relevant settings'
	oauth_web = request.GET['oauth_web']
	request.session['oauth_web'] = oauth_web
	settings = oauth_settings.form_params(oauth_web)
	request.session['settings'] = settings

	print 'init OAuth2Session'
	client_id = settings['client_id']
	client = settings['client']
	scope = settings['scope']	
	redirect_uri = settings['redirect_uri']
	token = settings['token']

	oa_session = OAuth2Session(client_id=client_id, client=client, scope=scope, redirect_uri=redirect_uri, token=token)
	
	#form the authorization_url
	auth_url = settings['auth_url']
	authorization_url, auth_state = oa_session.authorization_url(url=auth_url)

	print '[debug]:finishing form authorization_url, redirect to the page...'
	return HttpResponseRedirect(authorization_url)

def callback(request):

	if (request.method == 'GET'):# and (request.session.get('authorization_state',-1) != -1):  
		auth_response = 'http://127.0.0.1:5000'+request.get_full_path()
		request.session['auth_response'] = auth_response
		
		return get_token(request)
		
	else:
		raise render(request,'app/index_t.html',{'form':loginform})


def get_token(request):

	print 'enter get_token'

	oauth_web = request.GET['oauth_web']
	settings = oauth_settings.form_params(oauth_web)

	client_id = settings['client_id']
	client = settings['client']
	scope = settings['scope']	
	redirect_uri = settings['redirect_uri']
	token = settings['token']
	auth_state = request.GET['state']

	auth_session = OAuth2Session(client_id=client_id, client=client, scope=scope, redirect_uri=redirect_uri, token=token, state=auth_state)
	
	#fetch_token
	token_url=settings['token_url']
	# body=settings['body']
	auth=settings['auth']
	client_secret=settings['client_secret']
	# method=settings['method']
	# headers=settings['headers']
	timeout=settings['timeout']
	# verify=settings['verify']
	#!!!!important auth_response is get from the request.session
	auth_response=request.session['auth_response']
	print 'access_token'

	access_token = auth_session.fetch_token(token_url=token_url, auth=auth, client_id=client_id, client_secret=client_secret, timeout=timeout, authorization_response=auth_response)
	# access_token = auth_session.fetch_token(token_url=token_url, body=body, auth=auth, client_id=client_id, client_secret=client_secret, method=method, headers=headers, timeout=timeout, verify=verify, authorization_response=auth_response)

	#use token to get infomation
	print '[debug]:get token success'
	request.session['access_token'] = access_token

	getinfo_url = settings['getinfo_url']
	auth = OAuth2(client_id=client_id,token=access_token)
	paramss = {'source': client_id}

	infomation = requests.get(getinfo_url,auth=auth,params=paramss).json()
	print infomation

	info = {}

	if infomation.get('error',False):
		info['error_code'] = infomation['error_code']
		info['error'] = infomation['error']		
	else:
		displayInfo = settings['displayInfo']
		for elem in displayInfo:
			info[elem] = infomation[elem]
	
	#display info
	print '[debug]:get the infomation and to display'
	return render(request,'app/showinfo_t.html',{'info':info})


