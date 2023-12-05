from django.urls import path, re_path
from .views import index, user1, error

urlpatterns = [
    path('', index, name='home'),
    re_path(r'^user/(?P<login>\D+)/(?P<Name>\D+)/(?P<num>\d+)/', user1, name='user'),
    path('error/', error)
]
