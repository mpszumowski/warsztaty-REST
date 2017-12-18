from django.db import models


class Person(models.Model):

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        name = "{} {}".format(self.first_name, self.last_name)
        return name


class Movie(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(null=True)
    director = models.ForeignKey(Person,
                                 on_delete=True,
                                 related_name='movie_director')
    cast = models.ManyToManyField(Person,
                                  through='Role',
                                  related_name='movie_cast')
    year = models.IntegerField()


class Role(models.Model):

    person = models.ForeignKey(Person, on_delete=True)
    movie = models.ForeignKey(Movie, on_delete=True)
    character = models.CharField(max_length=64)


# Create your models here.
