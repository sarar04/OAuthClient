from django.conf.urls import patterns, url

from app import views
# from mysite import settings

# import settings

urlpatterns = patterns('',
	url(r'^$',								views.index,				name='index'),
	url(r'^mylogin/$',						views.mylogin,				name='mylogin'),
	url(r'^get_oauth_code/$',				views.get_oauth_code,		name='get_oauth_code'),
	url(r'^callback/$',						views.callback,				name='callback'),
)
