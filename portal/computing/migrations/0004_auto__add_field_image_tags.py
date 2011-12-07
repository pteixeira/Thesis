# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Image.tags'
        db.add_column('computing_image', 'tags', self.gf('tagging.fields.TagField')(default=''), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Image.tags'
        db.delete_column('computing_image', 'tags')


    models = {
        'computing.details_opennebula': {
            'Meta': {'object_name': 'Details_OpenNebula'},
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'dev_prefix': ('django.db.models.fields.CharField', [], {'default': "'hd'", 'max_length': '10'}),
            'driver': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'fstype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['computing.Image']"}),
            'image_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '500'}),
            'image_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'persistent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'computing.details_openstack': {
            'Meta': {'object_name': 'Details_OpenStack'},
            'architecture': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'container_format': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'disk_format': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['computing.Image']"}),
            'image_status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'kernel_id': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ramdisk_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        },
        'computing.image': {
            'Meta': {'object_name': 'Image'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'number_of_uses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'type_of_image': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['computing']
