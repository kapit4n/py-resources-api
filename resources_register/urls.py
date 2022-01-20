from django.urls import path
from .views import resources

urlpatterns = [
    path('resources/', resources, name="resources")
]
