from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Calories
from users.models import User


class CaloriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calories
        fields = ['date', 'time', 'text', 'date_created', 'number_of_calories',
                  'created_by', 'is_total_less_than_expected']
        read_only_fields = ('created_by', 'date_created')
