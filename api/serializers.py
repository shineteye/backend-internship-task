from rest_framework import serializers
from .models import Entry, CustomUser

# Serializer for entries


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'user', 'date', 'time',
                  'text', 'calories', 'is_below_expected']
        read_only_fields = ['id', 'is_below_expected']

    # def create(self, validated_data):
    #     # If calories are not provided, try to fetch from a calories API provider
    #     if 'calories' not in validated_data or validated_data['calories'] is None:
    #         validated_data['calories'] = fetch_calories_for_meal(validated_data['text'])

    #     return Entry.objects.create(**validated_data)

# Serializer for custom users


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email',
                  'expected_calories_per_day', 'is_superuser']
        read_only_fields = ['id', 'is_superuser']

    def update(self, instance, validated_data):
        # Prevent non-superusers from updating superuser status
        if not self.context['request'].user.is_superuser and 'is_superuser' in validated_data:
            validated_data.pop('is_superuser')

        return super().update(instance, validated_data)

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user
