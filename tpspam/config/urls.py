
from django.contrib import admin
from django.urls import path, include
from spam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spam/', include('spam.urls')),
]
