from rest_framework import serializers
from .models import Entry
from users.serializers import UserSerializer


class EntrySerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Entry
        fields = ['id', 'text', 'number_of_calories',
                  'is_calories_less_than_expected']

    def create(self, validated_data):
        user = self.context['request'].user
        number_of_calories = validated_data['number_of_calories']

        # user.profile.number_of_calories == to get the number of calories from the user profile
        if number_of_calories < 3000:
            # modified the boolean value
            validated_data['is_calories_less_than_expected'] = True

        entry = Entry.objects.create(
            # is_calories_less_than_expected=validated_data['is_calories_less_than_expected'],
            # # user=user,
            **validated_data
        )
        entry.save()
        return entry
