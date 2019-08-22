from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import CatsSerializer
from .models import Cat


@method_decorator(csrf_exempt, name='dispatch')
class CatViewSet(viewsets.ModelViewSet):

    serializer_class = CatsSerializer

    def get_queryset(self):
        # return Cat.objects.filter(owner=self.request.user)
        return Cat.objects.filter()
