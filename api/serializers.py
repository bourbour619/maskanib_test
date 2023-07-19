from rest_framework import serializers
from api.models import Index, IndexHistory

class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Index
        fields = '__all__'

class IndexHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = IndexHistory
        fields = '__all__'