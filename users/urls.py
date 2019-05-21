
from django.conf.urls import url
#from django.contrib.auth import login
from django.contrib.auth.views import LoginView  #非常重要
#from django.contrib.auth.views import RegisterView 
#from django.urls import path

from . import views
app_name='users'

urlpatterns = [
	url('login/', LoginView.as_view(template_name='users/login.html'), name='login'), 
	#url(r'^login/$', login, {'template_name':'users/login.html'},name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^register/$', views.register, name='register'),
	#url('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
	
]
