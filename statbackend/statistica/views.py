from django.shortcuts import render
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .models import Info
from .serializers import StatSerializer

# Create your views here.

class CustomFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        from_time = request.GET.get('from', None)
        to_time = request.GET.get('to', None)
        if from_time and to_time:
            return queryset.filter(date__gte=from_time, date__lte=to_time)
        else:
            return queryset.all()

class StatViewSet(ModelViewSet):
    '''
    ?from=&to=/
    '''

    queryset = Info.objects.all().order_by('-date')
    filter_backends = (CustomFilter,)
    serializer_class = StatSerializer
