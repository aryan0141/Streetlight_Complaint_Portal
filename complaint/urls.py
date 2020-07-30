from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
	path('admin/', admin.site.urls),	
	path("", views.index,name='index'),
    path("form", views.form,name='form'),
	path("submits", views.submits,name='submits'),
	path("login", views.login,name='login'),
	path("admins", views.admins,name='admins'),
	path("about", views.about,name='about')

	
]
