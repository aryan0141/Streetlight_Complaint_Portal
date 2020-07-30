from django.contrib import admin
from django.urls import path,include

urlpatterns = [
	path('', include('complaint.urls')),
	path('admin/', admin.site.urls),
]
