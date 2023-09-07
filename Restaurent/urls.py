from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
   path('', views.index, name='index'),
   path('menu-items/', views.MenuItemsView.as_view()),
   path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
   path('booking/', views.BookingsView.as_view()),
   path('booking/<int:pk>/', views.BookingView.as_view()),
   path('message/', views.secured_view),
   path('api-token-auth/', obtain_auth_token),
   # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]