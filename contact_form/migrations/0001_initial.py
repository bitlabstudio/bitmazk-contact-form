# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactFormCategory'
        db.create_table(u'contact_form_contactformcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=256)),
        ))
        db.send_create_signal(u'contact_form', ['ContactFormCategory'])

        # Adding model 'ContactFormCategoryTranslation'
        db.create_table(u'contact_form_contactformcategorytranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('contact_form_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact_form.ContactFormCategory'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'contact_form', ['ContactFormCategoryTranslation'])


    def backwards(self, orm):
        # Deleting model 'ContactFormCategory'
        db.delete_table(u'contact_form_contactformcategory')

        # Deleting model 'ContactFormCategoryTranslation'
        db.delete_table(u'contact_form_contactformcategorytranslation')


    models = {
        u'contact_form.contactformcategory': {
            'Meta': {'object_name': 'ContactFormCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256'})
        },
        u'contact_form.contactformcategorytranslation': {
            'Meta': {'object_name': 'ContactFormCategoryTranslation'},
            'contact_form_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact_form.ContactFormCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['contact_form']
