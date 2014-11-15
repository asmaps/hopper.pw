from django.db import models
from main.models import BaseModel


STAT_TYPES = (
    ('user_count', 'User count'),
    ('host_count', 'Host count'),
    ('ip_update_count', 'IP update count'),
)


class StatisticsEntry(BaseModel):
    class Meta:
        verbose_name_plural = 'Statistics Entries'

    stat_type = models.CharField(max_length=32, choices=STAT_TYPES)
    value = models.IntegerField()

    def __unicode__(self):
        return "%s: %d (%s)" % (self.stat_type, self.value, self.created)
