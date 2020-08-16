from django.urls import path
from .api.viewsets import Index, Store,Retrieve,Delete, Update

urlpatterns = [
    path('index', Index.as_view()),
    path('store', Store.as_view()),
    path('show/<int:id>', Retrieve.as_view()),
    path('delete/<int:id>', Delete.as_view()),
    path('update/<int:id>', Update.as_view()),

]