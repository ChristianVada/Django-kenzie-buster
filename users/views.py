from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.serializer import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


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


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(None, request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if not user:
            return Response(
                {"detail": "No active account found with the given credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)

        token_dict = {"refresh": str(refresh), "access": str(refresh.access_token)}

        return Response(token_dict, status.HTTP_200_OK)
