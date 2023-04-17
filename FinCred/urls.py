
from django.urls import path
from .import views



app_name= "FinCred"
urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('sign_up', views.sign_up, name="sign_up"),
     path('credit_details', views.credit_details, name='credit_details'),
    path('employment_details',views.employment_details, name="employment_details"),
    path('credit_score', views.credit_score, name="credit_score"),

]
