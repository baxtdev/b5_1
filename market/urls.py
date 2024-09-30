from django.urls import path,include

from .views import FakeAPIView
urlpatterns = [
    path('api/v1/fake-data/',FakeAPIView.as_view(),name="fake-endpoint"),
]
