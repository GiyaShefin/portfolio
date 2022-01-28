
from django.urls import path

from portfolio import views
app_name='portfolio'

urlpatterns = [
    path('',views.myportfolio,name='myportfolio'),
    path('details',views.details,name='details'),
    path('education',views.education,name='education'),
    path('personal',views.personal,name='personal'),
    path('certification',views.certification,name='certification'),
    ]