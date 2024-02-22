import re
from rest_framework import serializers
from .models import Book
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['publication_date'] > timezone.now().date():
            raise serializers.ValidationError("Date cannot be in future")
        
        pattern = r'^[a-zA-Z]'
        title = data['author']
        if not re.search(pattern, title):
            raise serializers.ValidationError("Do not use any special character")
        return data