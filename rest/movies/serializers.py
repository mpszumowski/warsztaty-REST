from rest_framework import serializers
from .models import Movie, Person, Role


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("first_name", "last_name")


class RoleSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source="person.first_name")
    last_name = serializers.ReadOnlyField(source="person.last_name")
    class Meta:
        model = Role
        fields = ("first_name", "last_name", "character")


class MovieSerializer(serializers.ModelSerializer):
    director = PersonSerializer(many=False, read_only=True)
    cast = RoleSerializer(source="role_set", many=True)
    class Meta:
        model = Movie
        fields = ("title", "description", "director", "cast", "year")
