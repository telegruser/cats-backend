from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import requests

from .serializers import CatsSerializer
from .serializers import CreateUserSerializer
from .models import Cat


CLIENT_ID = '1FeGEm1s6Tg1C5f5Yr9Ha4DVGqTAyyPi36pg9vYc'
CLIENT_SECRET = 'sNwNEXOJ8OtQZpE7D9HYcQHTMHZMIIrteQxGmUgSBfvRiu5JIpgCzqi6YSIguh6jnjlEZHfgM8NE1QH4K9jDQh3yNBn01TQ8mack' \
                'Zz4nDdKx4eDI9a7ceUn2ruUfqi1o'
AUTH_SERVER_URL = 'http://127.0.0.1:8000/'


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    {"username": "username", "password": "1234abcd"}
    """
    print("запрс регистрации: " + request.data)
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        r = requests.post(AUTH_SERVER_URL + 'o/token/', data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    """
    {"username": "username", "password": "1234abcd"}
    """
    r = requests.post(AUTH_SERVER_URL + 'o/token/', data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    print('запрос токена:' + str(request.data))
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    {"refresh_token": "<token>"}
    """
    r = requests.post(AUTH_SERVER_URL + 'o/token/', data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    """
    {"token": "<token>"}
    """
    print('запрос отзыва токена ' + str(request.data))
    r = requests.post(AUTH_SERVER_URL + 'o/revoke_token/', data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    if r.status_code == requests.codes.ok:
        print('токен отозван ' + str(request.data))
        return Response({'message': 'token revoked'}, r.status_code)
    print('не удалось отозвать токен ' + str(request.data))
    return Response(r.json(), r.status_code)


class CatViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CatsSerializer

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)
