from django.db import models
from main.models import BaseModel
import jsonfield


STAT_TYPES = (
    ('user_count', 'User count'),
)

class StatisticsEntry(BaseModel):
    stat_type = models.CharField(max_length=32, choices=STAT_TYPES)
    value = models.IntegerField()
