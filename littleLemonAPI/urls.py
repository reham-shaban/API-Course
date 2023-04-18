from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name='littleLemon'

urlpatterns = [
    path('menu-items', views.MenuItemsViewSet.as_view({'get':'list'})),
    path('menu-items/<int:pk>', views.MenuItemsViewSet.as_view({'get':'retrieve'})),
    path('api-token-auth/', obtain_auth_token),
    
    # path('menu-items', views.MenuItemsView.as_view()),
    # path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('categories', views.categories, name='categories'),
    # path('category/<int:pk>', views.category_detail, name='category-detail'),

]