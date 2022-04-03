
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

class MyTokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        # token['name'] = f'{user.first_name} {user.last_name}'
        token['email'] = user.email
        token['role_id'] = int(user.role_id)
        return token



class UserSerializer(serializers.ModelSerializer):

    ROLES = (
        (0, 'Patient'),
        (1, 'Doctor')
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)
    role_id = serializers.ChoiceField(default=0, choices=ROLES)

    class Meta:
        model = User
        fields = ('email', 'password', 'role_id')
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True},

        # }
    
    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         print("password is validated")
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs

    def create(self, validated_data):
        # data yang mau dimasukin ke database user
        user = User.objects.create(
            email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name'],
            role_id=validated_data['role_id']
        )
        
        user.set_password(validated_data['password'])
        print(validated_data)
        user.save()

        return user