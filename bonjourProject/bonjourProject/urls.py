

from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('/', hello, name='hello'),
]