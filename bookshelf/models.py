from django.db import models
from django.db.models import Manager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from core.models import AbstractTimeStampedModel


class Book(AbstractTimeStampedModel):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publishdate = models.DateField()
    description = models.CharField(
        'description',
        max_length=1000,
        null=True,
        blank=True)
    cover = models.ImageField(
        upload_to='images', 
        default=None, 
        null=True,
        blank=True)
