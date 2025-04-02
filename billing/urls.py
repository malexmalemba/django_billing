from django.urls import path 
from . import views


urlpatterns = [
    path ('',views.HomeView.as_view(), name='home'),
    path ('add-client',views.AddClientView.as_view(), name='add-client')
]