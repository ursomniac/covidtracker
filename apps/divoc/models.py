from django.db import models
from django.utils.translation import gettext as _
from ..meta.models import StateRegion

class DIVOCAbstract(models.Model):
    location = models.CharField (
        _('Location'),
        max_length = 100
    )
    case_date = models.DateField ()
    cases = models.FloatField (
        _('Cases'),
        help_text = 'cases per 100k, 7d average'
    )

    @property 
    def location_info(self):
        state = StateRegion.objects.filter(name=self.location).first()
        return state

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.case_date} - {self.location}: {self.cases}"

class DIVOCCase7DayAvg(DIVOCAbstract):
    class Meta:
        verbose_name = 'DIVOC Case (7d)'
        verbose_name_plural = 'DIVOC Cases (7d)'


class DIVOCCaseTotal(DIVOCAbstract):
    class Meta:
        verbose_name = 'DIVOC Case Total'
        verbose_name_plural = 'DIVOC Cases Total' 