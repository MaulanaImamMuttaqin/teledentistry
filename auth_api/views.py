
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, TokenObtainPairSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() :    
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response = {
                    "error" : None,
                    "code" : 200,
                    "data" : serializer.data,
                    "message" : "Success create new data"
                }
        else :
            response = {
                    "error" : None,
                    "code" : 400,
                    "message" : serializer.errors
            }

        return Response(response, status=status.HTTP_201_CREATED, headers=headers)



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
                "error" : None,
                "code" : 200,
                "data" : serializer.validated_data,
                "message" : "Success"
            }

            return Response(response, status=status.HTTP_200_OK)

        return Response({"error" : True}, status=status.HTTP_400_BAD_REQUEST)

# class LoginView()