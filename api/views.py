from rest_framework.response import Response
from .models import Gift, Category
from .serializers import GiftSerializer
from rest_framework.views import APIView



class GiftsFilterByManyCategories(APIView):
    def get(self, request, format=None):
        return Response({"Please use POST requests"})

    def post(self, request, format=None):
        filters = request.data['filters']
        if filters:
            categories = Category.objects.filter(name__in=filters)
            print(categories)
            gifts = Gift.objects.filter(category__in=categories).distinct()
            serializer = GiftSerializer(gifts, many=True)
            print(request.data)
            return Response(serializer.data)
        else:
            gifts = Gift.objects.all()
            serializer = GiftSerializer(gifts, many=True)
            return Response(serializer.data)
        
class GiftsFilterByOneCategory(GiftsListByManyCategories):
    pass