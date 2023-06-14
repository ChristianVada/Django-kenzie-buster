from rest_framework import serializers
from movies.models import Rating, Movie
from users.models import User


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(choices=Rating.choices, default=Rating.G)
    synopsis = serializers.CharField(required=False)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, instance: Movie):
        return instance.user.email

    def create(self, validate_data: dict) -> Movie:
        movie = Movie.objects.create(**validate_data)
        return movie
