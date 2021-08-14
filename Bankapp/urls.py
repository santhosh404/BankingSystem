from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('customers', views.Customer_Details, name='customers'),
    path('customer', views.Induival_Customer, name='indcustomer'),
    path('transaction', views.Transact, name='transaction'),
    path('history', views.History, name='history')
]