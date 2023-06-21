from rest_framework import viewsets

from .models import *
from .serializers import *

class ParentescoViewSet(viewsets.ModelViewSet):
    queryset = TblParentesco.objects.all()
    serializer_class = ParentescoSerializer

