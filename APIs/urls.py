from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from security.urls import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', v.login),
    
    path('api1/', include('BookList.urls', namespace='booklist')),
    path('api2/', include('security.urls', namespace='security')),
    path('api/', include('littleLemonAPI.urls', namespace='littleLemon')),
    
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('django.contrib.auth.urls')),
    
    path('api/', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    
    # path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

]
