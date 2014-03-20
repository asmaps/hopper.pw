# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'StatEntry'
        db.delete_table(u'stats_statentry')

        # Adding model 'StatusDataEntry'
        db.create_table(u'stats_statusdataentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('stat_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('data', self.gf('jsonfield.fields.JSONField')(default={})),
        ))
        db.send_create_signal(u'stats', ['StatusDataEntry'])


    def backwards(self, orm):
        # Adding model 'StatEntry'
        db.create_table(u'stats_statentry', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data', self.gf('jsonfield.fields.JSONField')(default={})),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('stat_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'stats', ['StatEntry'])

        # Deleting model 'StatusDataEntry'
        db.delete_table(u'stats_statusdataentry')


    models = {
        u'stats.statusdataentry': {
            'Meta': {'object_name': 'StatusDataEntry'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'stat_type': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['stats']