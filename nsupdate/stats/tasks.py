import datetime

from huey.djhuey import crontab, db_periodic_task, db_task
from django.conf import settings
from django.contrib.auth import get_user_model

from main.models import Host
from stats.models import StatisticsEntry


@db_periodic_task(crontab(hour='0', minute='0'))
def save_user_count():
    count = get_user_model().objects.all().count()
    StatisticsEntry.objects.create(stat_type='user_count', value=count)


@db_periodic_task(crontab(hour='0', minute='0'))
def save_host_count():
    count = Host.objects.all().count()
    StatisticsEntry.objects.create(stat_type='host_count', value=count)

@db_task()
def increment_ip_update_count():
    today = datetime.date.today()
    (se, created) = StatisticsEntry.objects.get_or_create(
            stat_type='ip_update_count',
            created__year=(today.year),
            created__month=(today.month),
            created__day=(today.day),
            defaults={'value': 0}
    )
    se.value = se.value + 1
    se.save()
