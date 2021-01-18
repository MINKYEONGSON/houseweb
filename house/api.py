from rest_framework import viewsets, serializers
from rest_framework.response import Response

from house.models import Apply, ApplyHomeType


class ApplyHomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyHomeType
        fields = (
            'id', 'name', 'price',
        )


class ApplySerializer(serializers.ModelSerializer):
    applyhometype_set = ApplyHomeTypeSerializer(many=True)

    class Meta:
        model = Apply
        fields = (
            'id', 'name', 'site', 'type1', 'type2',
            'publish_date', 'start_date', 'end_date',
            'address', 'home_count',
            'vote_tk', 'vote_1', 'vote_2', 'url',
            'applyhometype_set'
        )


class ApplyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer

    def list(self, request, *args, **kwargs):
        queryset = Apply.objects.all().order_by('site')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
