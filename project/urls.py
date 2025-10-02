from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('', include('contact.urls')), #Apontando pra url do contact
    path('admin/', admin.site.urls),
]
