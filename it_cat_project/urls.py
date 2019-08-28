from django.views.generic import TemplateView
from rest_framework import routers
from cat_app import views
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin


admin.autodiscover()

router = routers.DefaultRouter()
router.register('cats', views.CatViewSet, 'cats-list')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include(router.urls)),
    path('auth/', include('cat_app.urls')),
    url(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
]
