from django.db import models
from django.utils.translation import gettext as _

class USVaccination(models.Model):
    location = models.CharField (
        _('Location'),
        max_length = 100
    )
    sample_date = models.DateField ()
    total_vaccinations = models.FloatField (
        _('Tot. Vax'),
        null = True, blank = True
    )
    # First Vax
    people_vaccinated = models.FloatField (
        _('People Vax'),
        null = True, blank = True
    )
    people_vaccinated_per_hundred = models.FloatField (
        _('Vax 1 %'),
        null = True, blank = True
    )
    people_fully_vaccinated  = models.FloatField (
        _('People Vax 2'),
        null = True, blank = True
    )
    people_fully_vaccinated_per_hundred = models.FloatField (
        _('Vax 2 %'),
        null = True, blank = True
    )
    total_vaccinations_per_hundred = models.FloatField (
        _('Total Vax %'),
        null = True, blank = True
    )
    total_boosters = models.FloatField (
        _('Boosters'),
        null = True, blank = True
    )
    total_boosters_per_hundred = models.FloatField (
        _('Boosters %'),
        null = True, blank = True
    )
    """
    total_distributed
    distributed_per_hundred
    daily_vaccinations_raw
    daily_vaccinations
    daily_vaccinations_per_million
    share_doses_used
    """

    def __str__(self):
        p1 = f"{self.people_vaccinated_per_hundred}%" if self.people_vaccinated_per_hundred is not None else None
        p2 = f"{self.people_fully_vaccinated_per_hundred}%" if self.people_fully_vaccinated_per_hundred is not None else None
        p3 = f"{self.total_boosters_per_hundred}%" if self.total_boosters_per_hundred is not None else None
        return f"{self.sample_date} - {self.location}: ({p1}, {p2}, {p3})"

    class Meta:
        verbose_name = 'Vaccination (US)'
        verbose_name_plural = 'Vaccinations (US)'
