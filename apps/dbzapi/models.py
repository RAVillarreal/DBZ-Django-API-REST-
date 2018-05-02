from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    fight_lvl = models.IntegerField(verbose_name='Nivel de Pelea')
    height = models.FloatField(verbose_name='Altura (cm)')
    weight = models.FloatField(verbose_name='Peso (kg)')
    race = models.ForeignKey('Race', on_delete=models.CASCADE, verbose_name='Raza')
    techniques = models.ManyToManyField('Technique', verbose_name='Tecnicas')

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=50)
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Technique(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    damage = models.IntegerField()

    def __str__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=50)
    destroyed = models.BooleanField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
