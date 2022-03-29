
from asyncio.windows_events import NULL
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, TokenObtainPairSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
    
    # def post(self, *args, **kwargs):
    #     serializer = UserSerializer(data=self.request.data)
    #     if serializer.is_valid():
    #         get_user_model().objects.create_user(**serializer.validated_data)
    #         return Response(status=HTTP_201_CREATED)
    #     return Response(status=HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # try:
        #     serializer.is_valid(raise_exception=True)
        # except TokenError as e:
        #     raise InvalidToken(e.args[0])

        # return Response(serializer.validated_data, status=status.HTTP_200_OK)

        if serializer.is_valid(raise_exception= True):
            response = {
                "error" : NULL,
                "code" : 200,
                "data" : serializer.validated_data,
                "message" : "Success"
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response({"error" : True}, status=status.HTTP_400_BAD_REQUEST)

# class LoginView()