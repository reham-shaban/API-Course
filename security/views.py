from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# Create your views here.

@api_view()
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"some secret message"})


@api_view()
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def manager(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"only manager should see this"})
    else:
        return Response({"message":"you are not authorized"}, 403)


@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"successful"})
  
@api_view()
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_auth(request):
    return Response({"message":"successful for the logged in users"})
    
    
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)

