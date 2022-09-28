
from django.contrib import admin
from django.urls import path , include
from TVShows import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index ,name = 'home'),
    path('about',views.index ,name = 'about'),
    path('contacts',views.index ,name = 'contacts'),
    path('services',views.index ,name = 'services'),


]