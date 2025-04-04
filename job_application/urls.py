from django.urls import path
from . import views

# For home page
urlpatterns = [
    path('', views.index, name='index') 
]

# For about page
#urlpatterns = [
#    path('About', views.index, name='index') 
#]