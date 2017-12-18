from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer


class MoviesView(APIView):
    def all_movies(self):
        movies = Movie.objects.all()
        return movies

    def get(self, request, format=None):
        serializer = MovieSerializer(self.all_movies(),
                                     many=True,
                                     context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieView(APIView):
    def get_movie(self, id):
        try:
            return Movie.objects.get(pk=int(id))
        except Movie.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        movie = self.get_movie(id)
        serializer = MovieSerializer(movie,
                                     context={"request": request})
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = MovieSerializer(self.get_movie(id),
                                     context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        self.get_movie(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PeopleView(APIView):
    def get_people(self):
        return Person.objects.order_by("last_name")

    def get(self, request, format=None):
        serializer = PersonSerializer(self.get_people(),
                                      many=True,
                                      context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonView(APIView):
    def get_person(self, id):
        try:
            return Person.objects.get(pk=int(id))
        except Person.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        serializer = PersonSerializer(self.get_person(id),
                                      context={"request": request})
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = PersonSerializer(self.get_person(id),
                                      context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        self.get_person(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# Create your views here.
