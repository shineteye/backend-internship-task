from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Entry
from users.serializers import UserSerializer
from .validators import validate_text


class EntrySerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="entry-detail", lookup_field='pk')
    # email = serializers.EmailField(write_only=True)

    # we apply the validation this way as we import the validation from our own written validation module
    text = serializers.CharField(validators=[validate_text])
    # we can use this to grab the user who has logged in and get  the users email
    # we surely have to pass this into the fields list to prevent getting errors from that section
    # email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Entry
        fields = [
            # 'user',
            'edit_url',
            'url',
            'id',
            'text',
            'number_of_calories',
            'is_calories_less_than_expected'
        ]

    # for validation we use the validate keyword and then underscore and the field we want to validate
    # def validate_text(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     queryset = Entry.objects.filter(user=user, text__iexact=value)
    #     if queryset.exists():  # if the text is already in use we can then raise a validation error for that
    #         raise serializers.ValidationError(
    #             f"{value} is already in use")
    #     return value

    def get_edit_url(self, obj):
        # return f"/api/entries/{obj.pk }"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("entry-edit", kwargs={"pk": obj.id}, request=request)

    def create(self, validated_data):
        # it is used to get the user from the request being made
        # user = self.context['request'].user
        # email = validated_data['email']
        number_of_calories = validated_data['number_of_calories']

        # user.profile.number_of_calories == to get the number of calories from the user profile
        if number_of_calories < 3000:
            # modified the boolean value
            validated_data['is_calories_less_than_expected'] = True

        entry = Entry.objects.create(
            # is_calories_less_than_expected=validated_data['is_calories_less_than_expected'],
            # user=user,
            **validated_data
        )

        entry.save()
        return entry
