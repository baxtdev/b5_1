from django.urls import path,include

from .views import CategoryListApiView,CategoryDetailApiView
urlpatterns = [
    path('category/',CategoryListApiView.as_view(),name="category"),
    path('category/<int:pk>/', CategoryDetailApiView.as_view(),name="category-detail"),
]
