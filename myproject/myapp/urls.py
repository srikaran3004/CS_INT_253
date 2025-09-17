from django.urls import path, re_path
from . import views

urlpatterns = [
    # Basic routes without parameters
    path('', views.hello, name='hello'),
    path('home/', views.home1, name='home1'),
    path('home1/', views.home1, name='home1_alt'),
    path('dish/',  views.dish, name='dish'),
    path('itemDetails/',views.itemDetails,name='itemDetails'),
    path('form/', views.api_form, name='api_form'),
    path('addform/', views.add_form, name='add_form'),
    
    # Placement Portal Routes
    path('placement/', views.home, name='home'),
    path('placement/profile/', views.profile, name='profile'),
    path('placement/drives/', views.placement_drives, name='placement_drives'),
    
    # Routes with route parameters (URL path parameters)
    path('dish/<str:item>/',views.menuDisplay,name='menuDetails'),  # Route parameter: item
    path('dishDetails/<str:item_name>/', views.menu, name='menu'),  # Route parameter: item_name
    path('fetch/<int:id>/',views.fetch_data,name='fetch_data'),  # Route parameter: id
    
    # Route using regex with route parameters
    re_path(r'^lpu/(?P<year>\d{4})/(?P<month>\d{2})/$', views.lpu_info, name='lpu_info'),  # Route parameters: year and month
    
    # Routes that expect query parameters
    path('recipe/',views.recipe,name='recipe'),  # Expects query parameter like ?food=pizza
    path('add/', views.add_numbers, name='add_numbers'),  # Likely expects query parameters

    # Destinations Routes
    path('destinations/', views.destinations, name='destinations'),
    path('destinations/<str:place>/', views.destination_detail, name='destination_detail'),
]
