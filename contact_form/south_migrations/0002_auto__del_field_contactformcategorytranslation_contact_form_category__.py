# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ContactFormCategoryTranslation.contact_form_category'
        db.delete_column(u'contact_form_contactformcategorytranslation', 'contact_form_category_id')

        # Deleting field 'ContactFormCategoryTranslation.language'
        db.delete_column(u'contact_form_contactformcategorytranslation', 'language')

        # Adding field 'ContactFormCategoryTranslation.language_code'
        db.add_column(u'contact_form_contactformcategory_translation', 'language_code',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=15, db_index=True),
                      keep_default=False)

        # Adding field 'ContactFormCategoryTranslation.master'
        db.add_column(u'contact_form_contactformcategory_translation', 'master',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['contact_form.ContactFormCategory']),
                      keep_default=False)

        # Adding unique constraint on 'ContactFormCategoryTranslation', fields ['language_code', 'master']
        db.create_unique(u'contact_form_contactformcategory_translation', ['language_code', 'master_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ContactFormCategoryTranslation', fields ['language_code', 'master']
        db.delete_unique(u'contact_form_contactformcategory_translation', ['language_code', 'master_id'])


        # User chose to not deal with backwards NULL issues for 'ContactFormCategoryTranslation.contact_form_category'
        raise RuntimeError("Cannot reverse this migration. 'ContactFormCategoryTranslation.contact_form_category' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContactFormCategoryTranslation.contact_form_category'
        db.add_column(u'contact_form_contactformcategorytranslation', 'contact_form_category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact_form.ContactFormCategory']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ContactFormCategoryTranslation.language'
        raise RuntimeError("Cannot reverse this migration. 'ContactFormCategoryTranslation.language' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContactFormCategoryTranslation.language'
        db.add_column(u'contact_form_contactformcategorytranslation', 'language',
                      self.gf('django.db.models.fields.CharField')(max_length=16),
                      keep_default=False)

        # Deleting field 'ContactFormCategoryTranslation.language_code'
        db.delete_column(u'contact_form_contactformcategory_translation', 'language_code')

        # Deleting field 'ContactFormCategoryTranslation.master'
        db.delete_column(u'contact_form_contactformcategory_translation', 'master_id')


    models = {
        u'contact_form.contactformcategory': {
            'Meta': {'object_name': 'ContactFormCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256'})
        },
        u'contact_form.contactformcategorytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ContactFormCategoryTranslation', 'db_table': "u'contact_form_contactformcategory_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['contact_form.ContactFormCategory']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['contact_form']