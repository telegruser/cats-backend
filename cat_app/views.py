from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from cat_app.permissions import IsAuthenticatedOrCreate
from .serializers import CatsSerializer, RegistrationSerializer
from .models import Cat
from django.http import HttpResponse


# class LogInUser(viewsets.ModelViewSet):
#
#     permission_classes = [AllowAny]
#     serializer_class = LogInSerializer
#
#     """ Представление которое отвечает конечной точке API """
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Hello, OAuth2!')


# @method_decorator(csrf_exempt, name='dispatch')
class CatViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CatsSerializer
    # authentication_classes = [OAuth2Authentication]

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)
        # return Cat.objects.filter()


# class LogInView(generics.CreateAPIView):
#     # queryset = User.objects.all()
#     serializer_class = LogInSerializer
#     permission_classes = (IsAuthenticatedOrCreate,)
#
#     def get_queryset(self):
#         return


class RegisterViewSet(CreateModelMixin, GenericViewSet):
    model = User
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]
