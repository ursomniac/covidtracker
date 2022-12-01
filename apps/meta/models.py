from django.db import models
from django.utils.translation import gettext as _

COUNTRY_CHOICES = [
    ('US', 'USA'),
    ('CA', 'Canada')
]
LOCATION_CLASS_CHOICES = [
    ('us-state', 'US State'),
    ('us-region', 'US Region'), # includes US as a whole
    ('us-other', 'US Other'),
    ('ca-province', 'Canada Province'),
    ('canada', 'Canada'),
    ('us-county', 'County')
]

class StateRegionAbstract(models.Model):
    name = models.CharField (
        _('Location'),
        max_length = 100,
        unique = True
    )
    abbreviation = models.CharField (
        _('Abbreviation'),
        max_length = 10,
        null=True, blank=True
    )
    population = models.PositiveIntegerField (
        _('Population'),
        null = True, blank = True
    )
    country = models.CharField (
        _('Country'),
        max_length = 2,
        choices = COUNTRY_CHOICES
    )
    location_class = models.CharField (
        _('Location Class'),
        max_length = 40,
        choices = LOCATION_CLASS_CHOICES
    )
    swing_2016 = models.FloatField (
        _('Swing 2016'),
        null = True, blank = True
    )
    swing_2020 = models.FloatField (
        _('Swing 2020'),
        null = True, blank = True
    )
    swing_2022 = models.FloatField (
        _('Swing 2022'),
        null = True, blank = True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class StateRegion(StateRegionAbstract):
    pass

    class Meta:
        ordering = ['-country', 'name']
        verbose_name = 'State/Region/Province'
        verbose_name_plural = 'States/Regions/Provinces'

class USCounty(StateRegionAbstract):
    state = models.CharField (
        _('State'),
        max_length = 100
    )

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'US Counties'
