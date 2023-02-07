from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personal', views.personal, name='personal'),
    path('educational', views.educational, name='educational'),
    path('interests', views.interests, name='interests'),
    path('sell', views.sell, name='sell'),
    path('rolemodel', views.rolemodel, name='rolemodel'),
    path('showMydata', views.showMyData, name='showMyData'),
    path('listProduct', views.listProduct, name='listProduct'),
    path('inputProduct', views.inputProduct, name='inputProduct'),
    path('showGoodsList', views.showGoodsList, name='showGoodsList'),
    path('<gid>/showGoodsOne', views.showGoodsOne, name='showGoodsOne'),
    path('newGoods', views.newGoods, name='newGoods'),
    path('<gid>/updateGoods', views.updateGoods, name='updateGoods'),
    # path('<gid>/deleteGoods', views.deleteGoods, name='deleteGoods'),
    # path('showCustomerList', views.showCustomerList, name='showCustomerList'),
    # path('<gid>/showCustomerOne', views.showCustomerOne, name='showCustomerOne'),
    # path('newCustomer', views.newCustomer, name='newCustomer'),
    # path('<gid>/updateCustomer', views.updateCustomer, name='updateCustomer'),
    # path('<gid>/deleteCustomer', views.deleteCustomer, name='deleteCustomer'),
]
