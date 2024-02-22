import re
from rest_framework import serializers
from .models import Book,Review
from django.utils import timezone

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating']
    

class BookSerializer(serializers.ModelSerializer):
    review = ReviewSerializer()
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
        # depth=1
    
    def get_reviews(self, obj):
        reviews = Review.objects.get(id = obj.review.id)
        return {'Review':reviews.review}


    def validate(self, data):
        if data['publication_date'] > timezone.now().date():
            raise serializers.ValidationError("Date cannot be in future")
        
        pattern = r'^[a-zA-Z]'
        title = data['author']
        if not re.search(pattern, title):
            raise serializers.ValidationError("Do not use any special character")
        return data