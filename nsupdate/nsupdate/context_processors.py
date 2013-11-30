# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site


def add_settings(request):
    context = {}
    context['WWW_IPV4_HOST'] = settings.WWW_IPV4_HOST
    context['WWW_IPV6_HOST'] = settings.WWW_IPV6_HOST
    try:
        context['ENABLE_TRACKING'] = settings.ENABLE_TRACKING
    except:
        pass
    try:
        context['ENABLE_ADS'] = settings.ENABLE_ADS
    except:
        pass
    return context


def site(request):
    return {
        'site': Site.objects.get_current()
    }
