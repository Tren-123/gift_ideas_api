from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Gift
from .serializers import GiftSerializer
from django.http import JsonResponse


@api_view(['GET'])
def gift_list(request):
    if request.method == 'GET':
        gifts = Gift.objects.all()
        serializer = GiftSerializer(gifts, many=True)
        print(request.query_params)
        return Response(serializer.data)


