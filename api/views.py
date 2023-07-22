from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from api.models import Index, IndexHistory
from api.serializers import IndexSerializer, IndexHistorySerializer

# Create your views here.


class IndexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer


class IndexHistoryList(generics.ListAPIView):
    serializer_class = IndexHistorySerializer

    def get_queryset(self):
        ins_code = self.kwargs.get('ins_code')
        try:
            index = Index.objects.get(ins_code=ins_code)
        except Index.DoesNotExist:
            raise NotFound
        return IndexHistory.objects.filter(index=index)
