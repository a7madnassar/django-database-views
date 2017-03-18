# -*- coding: utf-8 -*-

from django.db import models


class AbstractTemplate(models.Model):
    """
    An abstract model class that represents a database template for a single app.

    Attributes:
        key: String - A unique identifier for the template.
        value: String - The template contents.
        gitsha: Binary - Reserved for future use for storing a git SHA.
        deployer: String - Reserved for future use for storing deployed info.
        created_at: Datetime - Creation date
    """
    key = models.CharField(max_length=255, unique=True, null=False)
    value = models.TextField(null=False)
    gitsha = models.BinaryField(max_length=20)
    deployer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AbstractApplicationTemplate(AbstractTemplate):
    """
    An abstract model that represent a database template for multiple apps.
    """
    app_name = models.CharField(max_length=255)
    current = models.BooleanField(default=False)

    class Meta:
        abstract = True



