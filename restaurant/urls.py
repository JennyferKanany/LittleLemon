#define URL route for index() view
from django.urls import path
from . import views
#import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('tables/<int:pk>', views.SingleBookingTableView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
