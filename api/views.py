import logging
from rest_framework.response import Response
from .models import Gift, Category
from .serializers import GiftSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ParseError
from django.utils.datastructures import MultiValueDictKeyError


logger = logging.getLogger(__name__)


class GiftsFilterByManyCategories(ListAPIView):
    serializer_class = GiftSerializer

    def get_queryset(self):
        logger.debug(self.request.query_params)
        filters = self.request.query_params.get("filters", None)
        logger.debug(filters)
        if filters:
            filters_list = list(filters.split(','))
            categories = Category.objects.filter(name__in=filters_list)
            logger.debug(categories)
            gifts = Gift.objects.filter(category__in=categories).distinct()
        else:
            text = f"'filters' not in query params. Query params: {self.request.query_params}"
            logger.error(text)
            raise ParseError(text)   
        return gifts
    
class GiftsFilterByOneCategory(GiftsFilterByManyCategories):
    pass