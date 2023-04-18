from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name='security'

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('secret', views.secret),
    path('manager-view', views.manager),
    path('throttle-check', views.throttle_check),
    path('throttle-check-auth', views.throttle_check_auth),
]