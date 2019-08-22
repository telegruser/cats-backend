from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from rest_framework import routers
from cat_app import views
# from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
router.register('cats', views.CatViewSet, 'cats-list')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    url(r'home/', TemplateView.as_view(template_name="home.html"), name="home")
]
