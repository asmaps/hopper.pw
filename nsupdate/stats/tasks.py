from huey.djhuey import crontab, periodic_task, task
from django.conf import settings
from django.contrib.auth import get_user_model
from stats.models import StatisticsEntry


@periodic_task(crontab(hour='0', minute='0'))
def save_user_count():
    count = get_user_model().objects.all().count()
    sdt = StatisticsEntry.objects.create(stat_type='user_count', value=count)
