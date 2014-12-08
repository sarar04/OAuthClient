#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class loginform(forms.Form):
	username = forms.CharField(label="username",max_length=20)
	password = forms.CharField(label="password",max_length=20,widget=forms.PasswordInput)

	def login_valid(self,username,password):
		if (username == 'admin' and password == 'admin') or (username == 'sarar' and password == 'sarar') or (username == 'guest' and password == 'guest'):
			return True
		else:
			return False

ACTIVITY_STYLE = (("0","头像"),("1", "注册时间"), ("2", "个人主页"), ("3", "邮箱"))  

class chooseform(forms.Form):
    selections = forms.MultipleChoiceField(choices=ACTIVITY_STYLE, widget=forms.CheckboxSelectMultiple())
	
