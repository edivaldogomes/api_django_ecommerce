from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.api.serializers import User
from apps.users.api.serializers import UserSerializer


class UserAPIView(APIView):

    def get(self, request):
        user = User.objects.all()
        users_serializer = UserSerializer(user, many=True)
        return Response(users_serializer.data)


@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        user = User.objects.all()
        users_serializer = UserSerializer(user, many=True)
        return Response(users_serializer.data)
    elif request.method == 'POST':
        print(request.data)
