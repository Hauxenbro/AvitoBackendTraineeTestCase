from rest_framework import serializers
from .models import Info

class StatSerializer(serializers.ModelSerializer):
    cpc = serializers.SerializerMethodField(read_only=True)
    cpm = serializers.SerializerMethodField(read_only=True)

    def get_cpc(self, obj):
        clicks = obj.clicks
        cost = obj.cost
        if clicks != 0 and cost != 0:
            return float(f"{cost/clicks:.2f}")
        else:
            return 0

    def get_cpm(self, obj):
        views = obj.views
        cost = obj.cost
        if views != 0 and cost != 0:
            return float(f"{cost / views:.2f}") * 1000
        else:
            return 0

    class Meta:
        model = Info
        url = serializers.HyperlinkedIdentityField(view_name='info-detail')
        fields = ('date', 'views', 'clicks', 'cost', 'cpc', 'cpm','url')