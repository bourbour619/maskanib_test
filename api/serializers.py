from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.models import Index, IndexHistory
from datetime import datetime

class TseTmcIndexSerializer(serializers.Serializer):
    insCode = serializers.CharField(
        max_length=20,
        source='ins_code',
        validators=[UniqueValidator(queryset=Index.objects.all())]
    )
    lVal30 = serializers.CharField(max_length=40, source='lval30')

    def create(self, validated_data):
        return Index.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ins_code = validated_data.get('insCode', instance.ins_code)
        instance.lval30 = validated_data.get('lVal30', instance.lval30)
        instance.save()
        return instance
        


class TseTmcIndexHistorySerializer(serializers.Serializer):
    insCode = serializers.CharField(max_length=20, source='index_id')
    dEven = serializers.CharField(max_length=8, source='date')
    xNivInuClMresIbs = serializers.DecimalField(max_digits=8, decimal_places=1, source='close')
    xNivInuPbMresIbs = serializers.DecimalField(max_digits=8, decimal_places=1, source='low')
    xNivInuPhMresIbs = serializers.DecimalField(max_digits=8, decimal_places=1, source='high')


    def validate(self, attrs):
        try:
            IndexHistory.objects.get(**attrs)
            raise serializers.ValidationError('Duplicated history.')
        except IndexHistory.DoesNotExist:
            return attrs


    def create(self, validated_data):
        validated_data['date'] = self.deven_to_date(validated_data.get('date'))
        ins_code = validated_data.pop('index_id')
        try:
            index = Index.objects.get(ins_code=ins_code)
            return IndexHistory.objects.create(index=index, **validated_data)
        except Index.DoesNotExist:
            return None

    def update(self, instance, validated_data):
        instance.low = validated_data.get('low', instance.low)
        instance.high = validated_data.get('high', instance.high)
        instance.close = validated_data.get('close', instance.close)
        instance.save()
        return instance

    def deven_to_date(self, deven):
        dt = '{0}-{1}-{2}'.format(deven[0:4], deven[4:6], deven[6:8])
        return datetime.strptime(dt, '%Y-%m-%d').date()

class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Index
        exclude = ['id']

class IndexHistorySerializer(serializers.ModelSerializer):
    ins_code = serializers.CharField(source='index_id', read_only=True)

    class Meta:
        model = IndexHistory
        exclude = ['id', 'index']