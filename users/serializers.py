from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User


class UserSerializer(serializers.ModelSerializer):

    # calories = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Calories.objects.all())

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name',
                  'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        # Ensuring that tokens are created when user is created in UserCreate view, so we update the UserSerializer.
        Token.objects.create(user=user)
        return user
