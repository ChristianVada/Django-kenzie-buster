from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.serializer import UserSerializer


class UserView(APIView):
    def get(self, request: Request) -> Response:
        accounts = User.objects.all()

        serializer = UserSerializer(accounts, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(None, request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
