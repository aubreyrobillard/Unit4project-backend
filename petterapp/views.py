from .models import Petter
from rest_framework import permissions
from rest_framework import viewsets
from .serializers import PetterSerializer


# Create your views here.
class PetterViewSet(viewsets.ModelViewSet):
    queryset = Petter.objects.all()
    serializer_class = PetterSerializer
    permission_classes = [permissions.AllowAny]
