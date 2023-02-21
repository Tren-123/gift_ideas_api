import logging
from rest_framework.response import Response
from .models import Gift, Category
from .serializers import GiftSerializer
from rest_framework.views import APIView


logger = logging.getLogger(__name__)


class GiftsFilterByManyCategories(APIView):
    def get(self, request, format=None):
        return Response({"Please use POST requests"})

    def post(self, request, format=None):
        logger.debug(request.data)
        try:
            filters = request.data['filters']
            if filters:
                categories = Category.objects.filter(name__in=filters)
                logger.debug(categories)
                gifts = Gift.objects.filter(category__in=categories).distinct()
                serializer = GiftSerializer(gifts, many=True)
                return Response(serializer.data)
            else:
                gifts = Gift.objects.all()
                serializer = GiftSerializer(gifts, many=True)
                return Response(serializer.data)
        except (KeyError, TypeError) as e:
            logger.error(f"{type(e).__name__}: {e}")
            return Response({"Body of request should contain dict with 'filters' key"})

class GiftsFilterByOneCategory(GiftsFilterByManyCategories):
    pass