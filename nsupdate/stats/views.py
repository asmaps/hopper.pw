from django.views.generic import TemplateView
from .models import StatisticsEntry

class StatsView(TemplateView):
    template_name = 'stats/stats.html'
    
    def get_context_data(self, **kwargs):
        context = super(StatsView, self).get_context_data(**kwargs)
        context['user_counts'] = StatisticsEntry.objects.filter(stat_type='user_count').order_by('created')
        return context
