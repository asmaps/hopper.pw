# coding=utf-8
from django.contrib import admin

from main.models import Host, Domain, BlacklistedDomain


class HostAdmin(admin.ModelAdmin):
    search_fields = ['subdomain', 'domain']
    list_fields = ['get_fqdn', 'created_by']

admin.site.register(BlacklistedDomain)
admin.site.register(Domain)
admin.site.register(Host, HostAdmin)
