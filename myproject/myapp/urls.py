from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('home/', views.home1, name='home1'),
    path('home1/', views.home1, name='home1_alt'),
    path('dish/',  views.dish, name='dish'),
    path('itemDetails/',views.itemDetails,name='itemDetails'),
    path('dish/<str:item>/',views.menuDisplay,name='menuDetails'), #using query params
    path('dishDetails/<str:item_name>/', views.menu, name='menu'), #using if esle
    path('form/', views.api_form, name='api_form'),
    path('fetch/<int:id>/',views.fetch_data,name='fetch_data'),
    path('addform/', views.add_form, name='add_form'),
    path('add/', views.add_numbers, name='add_numbers'),
]
