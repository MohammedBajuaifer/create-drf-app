from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets, response
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.serializers import UserSerializer, CreateUserSerializer


User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer


class WhoamiViewSet(viewsets.ViewSet):

    """
    View to return the current user.
    * Requires token authentication.
    """
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = User.objects.get(id=self.request.user.id)
        serializer = UserSerializer(queryset)
        return response.Response(serializer.data)