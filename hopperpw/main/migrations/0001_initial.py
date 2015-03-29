# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistedDomain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('domain', models.CharField(help_text=b'Blacklisted domain. Evaluated as regex (search).', unique=True, max_length=256)),
                ('created_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('domain', models.CharField(unique=True, max_length=256)),
                ('nameserver_ip', models.IPAddressField()),
                ('nameserver_update_key', models.CharField(max_length=256, validators=[main.models.ns_update_key_validator])),
                ('nameserver_update_algorithm', models.CharField(max_length=256, choices=[(b'HMAC_SHA512', b'HMAC_SHA512')])),
                ('available_for_everyone', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subdomain', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator(regex=b'^(([a-z0-9][a-z0-9\\-]*[a-z0-9])|[a-z0-9])$', message=b'Invalid subdomain: only "a-z", "0-9" and "-" is allowed'), main.models.domain_blacklist_validator])),
                ('update_secret', models.CharField(max_length=256)),
                ('comment', models.CharField(default=b'', max_length=256, null=True, blank=True)),
                ('last_api_update', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('domain', models.ForeignKey(to='main.Domain')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='host',
            unique_together=set([('subdomain', 'domain')]),
        ),
    ]
