from .models import Entry
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# for validation we use the validate keyword and then underscore and the field we want to validate


def validate_text(value):
    queryset = Entry.objects.filter(text__iexact=value)
    if queryset.exists():  # if the text is already in use we can then raise a validation error for that
        raise serializers.ValidationError(
            f"{value} is already a text in use")
    return value


# another method to validate uniqueness
unique_entry_text = UniqueValidator(
    queryset=Entry.objects.all(), lookup='iexact')
