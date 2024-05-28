from .views import *
from django.urls import path

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('<int:pk>', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail')
]