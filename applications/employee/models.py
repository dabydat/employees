from django.db import models
from applications.department.models import Department

# Create your models here.


class Skills(models.Model):
    """Model definition for Skills."""

    skill = models.CharField('Skill', max_length=50)

    class Meta:
        """Meta definition for Skills."""

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        """Unicode representation of Skills."""
        return str(self.id) + ' ' + self.skill


class Employee(models.Model):
    """Model definition for Employee."""

    JOB_CHOICES = (
        ('0', 'Technical Support'),
        ('1', 'Developer'),
        ('2', 'System Administrator'),
        ('3', 'Cloud Engineer'),
        ('4', 'Teacher'),
        ('5', 'General Services'),
        ('6', 'Student'),
        ('7', 'Other'),
    )

    name = models.CharField('First Name', max_length=60)
    last_name = models.CharField('Last Name', max_length=60)
    age = models.IntegerField('Age')
    id_number = models.IntegerField(
        'ID Number', unique=True, blank=False, null=False)
    job_name = models.CharField('Job Name', max_length=60, choices=JOB_CHOICES)
    image = models.ImageField(
        'Employee Avatar', upload_to='employee', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)

    class Meta:
        """Meta definition for Employee."""

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['id']

    def __str__(self):
        """Unicode representation of Employee."""
        return str(self.id) + ' ' + self.name + ' ' + self.last_name
