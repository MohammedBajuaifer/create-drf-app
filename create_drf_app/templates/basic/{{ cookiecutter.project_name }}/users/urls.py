from django.urls import path, include

from rest_framework import routers

from users.views import CreateUserView
from users.views import  WhoamiViewSet

router = routers.DefaultRouter()

router.register(r'whoami', WhoamiViewSet, basename="whoami")

urlpatterns = [
    path('signup/', CreateUserView.as_view()),
    path('', include(router.urls))
]