from django.db import models
from django.utils import timezone


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    county = models.CharField(max_length=255)
    publishers = models.ManyToManyField(Publisher, related_name='authors', blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.CASCADE)
    size = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name='books', blank=True)

    def __str__(self):
        return self.title


class Tyrage(models.Model):
    date = models.DateField()
    amount = models.IntegerField()
    publisher = models.ForeignKey(Publisher, related_name='tyrages', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='tyrages', on_delete=models.CASCADE)

    def publish_tyrage(self):
        self.date = timezone.now
        self.save()


    def __str__(self):
        return '{} {}'.format(self.amount, self.publisher)
