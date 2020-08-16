from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProjetosIndexSerializer, ProjetosCreateUpdateSerializer, ProjetosRetrieveSerializer
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)
from projetos.models import Projetos
from rest_framework.permissions import IsAuthenticated

class Index(ListAPIView):
    serializer_class = ProjetosIndexSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    def get_queryset(self):
        return Projetos.objects.filter(user=self.request.user)

class Store(CreateAPIView):
    serializer_class = ProjetosCreateUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class Retrieve(RetrieveAPIView):

    serializer_class = ProjetosRetrieveSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"
    def get_queryset(self):
        return Projetos.objects.filter(user=self.request.user)

class Delete(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        queryset = Projetos.objects.filter(user=self.request.user, id=self.kwargs['id'])
        return queryset

    def perform_destroy(self, instance):
        instance.delete()

class Update(UpdateAPIView):
    serializer_class = ProjetosCreateUpdateSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        queryset = Projetos.objects.filter(user=self.request.user, id=self.kwargs['id'])
        return queryset

    def perform_update(self, serializer):
        serializer.save()











