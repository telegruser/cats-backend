# from django.contrib import admin
# from django.urls import include, path, re_path
# from django.conf.urls import url
# from django.views.generic.base import TemplateView
# from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import routers
from cat_app import views
# import cat_app
# from django.urls import path, include
# from django.contrib.auth.models import User, Group
# from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include
# import oauth2_provider.views as oauth2_views
# from django.conf import settings
# from cat_app.views import ApiEndpoint
from django.urls import path, include
from django.contrib.auth.models import User, Group
from django.contrib import admin

# from cat_app.models import Cat
# from cat_app.serializers import CatsSerializer
# from cat_app.views import CatViewSet

admin.autodiscover()

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


# Create the API views
class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


router = routers.DefaultRouter()
router.register('cats', views.CatViewSet, 'cats-list')
router.register('register', views.RegisterViewSet, 'register')
# router.register('api-endpoint', views.ApiEndpoint, 'api-endpoint')


# oauth2_endpoint_views = [
#     url(r'^authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
#     url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
#     url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
# ]
#
# if settings.DEBUG:
#     # OAuth2 Application Management endpoints
#     oauth2_endpoint_views += [
#         url(r'^applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
#         url(r'^applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
#         url(r'^applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
#         url(r'^applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
#         url(r'^applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
#     ]
#
#     # OAuth2 Token Management endpoints
#     oauth2_endpoint_views += [
#         url(r'^authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
#         url(r'^authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(),
#             name="authorized-token-delete"),
#     ]


# class CatViewSet(generics.QuerySet):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = User.objects.all()
#     serializer_class = CatsSerializer
#     # authentication_classes = [OAuth2Authentication]
#     # permission_classes = [TokenHasScope]
#
#     def get_queryset(self):
#         return Cat.objects.filter(owner=self.request.user)
#         # return Cat.objects.filter()
# from django.http.request import HttpRequest
#
# def sign_in_handler(request: HttpRequest):
#     print(request.headers)
#     print(request.body)
#     print(request.method)
#     return HttpResponse('ответ')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('sign-in/', sign_in_handler),
    path('api/', include(router.urls)),  # CatViewSet.as_view({'get': 'list', 'post': })),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
    url(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
]


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     # url(r'^user/register/$', views.UserRegister.as_view()),
#     # url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
#     url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
#
#     # url(r'^o/', include('cat_app.urls')),
#     url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
#     # url(r'^o/', include((oauth2_endpoint_views, 'oauth2'), namespace='oauth2_provider')),
#     url(r'^api/hello/', ApiEndpoint.as_view()),  # an example resource endpoint
#
#     url('^api/', include(router.urls)),
#     url(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
# ]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('accounts/', include('registration.urls', namespace="accounts")),
#     # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
#     # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
#     url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
#     path('api/', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     # url(r'^tmp/', TemplateView.as_view(template_name="registration/login.html"), name="home"),
#     url(r'', TemplateView.as_view(template_name="home.html"), name="home"),
#     # path('', TemplateView.as_view(template_name="cats.html"), name="cats"),
#     # path('users/', UserList.as_view()),
#     # path('users/<pk>/', UserDetails.as_view()),
#     # path('groups/', GroupList.as_view()),
# ]
