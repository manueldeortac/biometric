from django.db import models


class Register (models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    weight = models.IntegerField()

    heart_rate = models.IntegerField()
    oxygen_saturation = models.IntegerField()
    stress_level = models.IntegerField()