from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer
from apps.users.api.serializers import User
from rest_framework.response import Response


class UserAPIView(APIView):

    def get(self, request):
        user = User.objects.all()
        users_serializer = UserSerializer(user, many=True)
        return Response(users_serializer.data)