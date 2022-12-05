from django.db import models
from django.utils.translation import gettext as _

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

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.case_date} - {self.location}: {self.cases}"

class DIVOCAbstractPeak(models.Model):
    peak = models.FloatField (
        _('Peak Value'),
        null = True, 
        blank = True
    )

    class Meta:
        abstract = True

class DIVOCCase7DayAvg(DIVOCAbstract, DIVOCAbstractPeak):
    iscore = models.FloatField(_('IScore'), null=True, blank=True)
    iscore_raw = models.FloatField(_('Raw IScore'), null=True, blank=True)
    rscore = models.FloatField(_('RScore'), null=True, blank=True)
    vscore = models.FloatField(_('VScore'), null=True, blank=True)
    nscore = models.FloatField(_('NScore'), null=True, blank=True)


    class Meta:
        verbose_name = 'DIVOC Case (7d)'
        verbose_name_plural = 'DIVOC Cases (7d)'

class DIVOCCaseDaily(DIVOCAbstract, DIVOCAbstractPeak):
    class Meta:
        verbose_name = 'DIVOC Case Daily'
        verbose_name_plural = 'DIVOC Cases Daily'

class DIVOCCaseTotal(DIVOCAbstract):
    class Meta:
        verbose_name = 'DIVOC Case Total'
        verbose_name_plural = 'DIVOC Cases Total' 

