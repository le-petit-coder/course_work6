from functools import partial
from rest_framework import pagination, viewsets
from ads.models import Ad
from ads.serializers import AdSerializer, AdDetailSerializer
from rest_framework.views import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ads.permissions import UserPermission
from rest_framework.permissions import IsAuthenticated



class AdPagination(pagination.PageNumberPagination):
    page_size = 3


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    #permission_classes = [UserPermission]

    def list(self, request):
        queryset = Ad.objects.all()
        serializer = AdSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Ad.objects.all()

        user = get_object_or_404(queryset, pk=pk)
        serializer = AdDetailSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Ad.objects.all()

        user = get_object_or_404(queryset, pk=pk)

        serializer = AdSerializer(user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data)

    def partial_update(self, request, pk=None, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        queryset = Ad.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    pass

