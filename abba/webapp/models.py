from django.db import models


class Teacher(models.Model):

    KIND_CHOICES = (
        ('C', 'Contratado'),
        ('R', 'Regular'),
        ('A', 'Asociadp'),
        ('E', 'Emérito'),
    )

    DEDICATION_CHOICES = (
        ('C', 'Tiempo completo'),
        ('M', 'Medio tiempo'),
        ('H', 'Asignatura por horas'),
    )

    name = models.CharField(max_length=128)
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    dedication = models.CharField(max_length=1, choices=DEDICATION_CHOICES)


class Journal(models.Model):
    name = models.CharField(max_length=256)


class BibliographicDatabase(models.models):
    name = models.CharField(max_length=128)


class Article(models.Model):

    KIND_CHOICES = (
        ('T', 'Documento de trabajo'),
        ('R', 'Artículo de revista'),
        ('L', 'Libro'),
        ('P', 'Parte de libro'),
    )

    title = models.CharField(max_length=256)
    keywords = models.CharField(max_length=64)
    publication_date = models.DateTimeField()
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    journals = models.ManyToManyField(Journal)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    indexed_by = models.ManyToManyField(BibliographicDatabase)
    raw_languages = models.CharField(max_length=128)  # ISO 639-1
