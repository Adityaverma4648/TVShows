
from django.contrib import admin
from django.urls import path , include
from TVShows import views
# from tv_shows import 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index ,name = 'home'),
    path('about',views.about ,name = 'about'),
    path('contacts',views.contacts ,name = 'contacts'),
    path('services',views.services,name = 'services'),
]