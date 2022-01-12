from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django import forms
from .models import OrganizationProfile, CustomUser

# DOCS - https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/

'''
Form that uses built-in UserCreationForm to handel user creation
'''
class UserForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))
	last_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))
	# username = forms.EmailField(max_length=254, required=True,
	# 	widget=forms.TextInput(attrs={'placeholder': '*Username..'}))
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class':'password'}))
	email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Email..'}))

	class Meta:
		model = CustomUser
		fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )




'''
Form that uses built-in AuthenticationForm to handel user auth
'''
class AuthForm(forms.Form):
	
	email = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))

	# class Meta:
	# 	model = CustomUser
	# 	fields = ('email','password', )




'''
Basic model-form for our user profile that extends Django user model.
'''
class OrganizationProfileForm(forms.ModelForm):
	
	phone_number = forms.CharField(max_length=15, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Telephone..'}))
	address = forms.CharField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={'placeholder': '*First line of address..'}))
	city = forms.CharField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={'placeholder': '*Town or City..'}))
	country = forms.CharField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={'placeholder': '*Country..'}))
	organization_name = forms.CharField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={'placeholder': '*Organization Name..'}))


	class Meta:
		model = OrganizationProfile
		fields = ('phone_number', 'address', 'city', 'country', 'organization_name', )




'''
Form that uses built-in PasswordResetForm to handel a request to reset password
'''
class RequestPasswordForm(PasswordResetForm):
	
	email = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	
	class Meta:
		model = CustomUser
		fields = ('email',)




'''
Form that uses built-in SetPasswordForm to handel resetting passwords
'''
class ForgottenPasswordForm(SetPasswordForm):
	
	new_password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))
	new_password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class':'password'}))

	class Meta:
		model = CustomUser
		fields = ('password1', 'password2', )