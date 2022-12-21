from .models import Pagos2
from rest_framework import viewsets
from .serializers import Pago2Serializer
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 


class Pago2ViewSet(viewsets.ModelViewSet):
    queryset = Pagos2.objects.get_queryset().order_by('id')
    serializer_class = Pago2Serializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    search_fields = []
    throttle_scope = 'pagos'