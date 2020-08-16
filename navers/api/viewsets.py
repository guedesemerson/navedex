from django_filters.rest_framework import DjangoFilterBackend
from .serializers import NaversIndexSerializer, NaveGenericSerializer, NaveRetrieveSerializer
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)
from navers.models import Naver
from rest_framework.permissions import IsAuthenticated


class Index(ListAPIView):

    serializer_class = NaversIndexSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'admission_date', 'job_role']

    def get_queryset(self):
        return Naver.objects.filter(user=self.request.user)

class Retrieve(RetrieveAPIView):

    serializer_class = NaveRetrieveSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"
    def get_queryset(self):
        return Naver.objects.filter(user=self.request.user)

class Store(CreateAPIView):
    serializer_class = NaveGenericSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class Delete(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        queryset = Naver.objects.filter(user=self.request.user, id=self.kwargs['id'])
        return queryset

    def perform_destroy(self, instance):
        instance.delete()

class Update(UpdateAPIView):
    serializer_class = NaveGenericSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        queryset = Naver.objects.filter(user=self.request.user, id=self.kwargs['id'])
        return queryset

    def perform_update(self, serializer):
        serializer.save()











