from rest_framework import viewsets

from .models import *
from .serializers import *

class ParentescoViewSet(viewsets.ModelViewSet):
    queryset = TblParentesco.objects.all()
    serializer_class = ParentescoSerializer
    
class ApoderadoViewSet(viewsets.ModelViewSet):
    queryset = TblApoderado.objects.all()
    serializer_class = ApoderadoSerializer

