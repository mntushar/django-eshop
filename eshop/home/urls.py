from django.urls import path
from .import views

urlpatterns = [
    path('', views.user_home, name='home-deshboard'), #user home url
    path('carditem/<int:pk>/', views.addcard, name='add-item-card'), #add item in card url
    path('itemremove/<int:pk>/', views.removecard, name='remove-item-card'), #remove item in card url
    path('listcard/', views.card, name='card-list'), #card list url
    path('removeitem/<int:pk>', views.card_item_remove, name='remove-card-item'), #remove item insert care url
    

]