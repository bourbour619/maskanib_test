from rest_framework import viewsets, permissions
from api.models import Index, IndexHistory
from api.serializers import IndexSerializer

# Create your views here.

class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer
    permission_classes = [permissions.AllowAny]