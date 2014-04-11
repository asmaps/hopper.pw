from django.views.generic import TemplateView
from .models import StatisticsEntry

class StatsView(TemplateView):
    template_name = 'stats/stats.html'
    
    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)
        context['user_counts'] = StatisticsEntry.objects.filter(stat_type='user_count').order_by('created')[:30]
        context['host_counts'] = StatisticsEntry.objects.filter(stat_type='host_count').order_by('created')[:30]
        context['ip_update_counts'] = list(StatisticsEntry.objects.filter(stat_type='ip_update_count').order_by('created'))[-31:-1]
        context['nav_stats'] = True
        return context
