from django.db import models

# Create your models here.


class Department(models.Model):
    """Model definition for Department."""

    name = models.CharField('Department Name', max_length=60)
    short_name = models.CharField('Department Acronym', max_length=30)

    class Meta:
        """Meta definition for Department."""

        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        """Unicode representation of Department."""
        return self.name
