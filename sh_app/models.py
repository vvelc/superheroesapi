from django.db import models


class SuperHero(models.Model):
    hero_name = models.CharField(max_length=100, unique=True)
    superpower1 = models.CharField(max_length=25)
    superpower2 = models.CharField(max_length=25)
    weakness1 = models.CharField(max_length=25)
    weakness2 = models.CharField(max_length=25)
    hero_age = models.IntegerField()
    hero_image = models.ImageField(upload_to='static/hero_images', default='http://via.placeholder.com/300')
    GENDER_CHOICES = [
        ('Female','FEMALE'),
        ('Male','MALE')
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male')
    secret_identity = models.CharField(max_length=255)