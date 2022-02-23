from django.urls import path
from user.views import Join

urlpatterns = [
    path('join', Join.as_view())
]
