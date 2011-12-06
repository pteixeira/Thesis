# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Image'
        db.create_table('computing_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('type_of_image', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('number_of_uses', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('computing', ['Image'])

        # Adding model 'Details_OpenStack'
        db.create_table('computing_details_openstack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['computing.Image'])),
            ('kernel_id', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('image_status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ramdisk_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('architecture', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('container_format', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('disk_format', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('computing', ['Details_OpenStack'])

        # Adding model 'Details_OpenNebula'
        db.create_table('computing_details_opennebula', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=500)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('image_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('persistent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dev_prefix', self.gf('django.db.models.fields.CharField')(default='hd', max_length=10)),
            ('bus', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('driver', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('fstype', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('computing', ['Details_OpenNebula'])


    def backwards(self, orm):
        
        # Deleting model 'Image'
        db.delete_table('computing_image')

        # Deleting model 'Details_OpenStack'
        db.delete_table('computing_details_openstack')

        # Deleting model 'Details_OpenNebula'
        db.delete_table('computing_details_opennebula')


    models = {
        'computing.details_opennebula': {
            'Meta': {'object_name': 'Details_OpenNebula'},
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'dev_prefix': ('django.db.models.fields.CharField', [], {'default': "'hd'", 'max_length': '10'}),
            'driver': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'fstype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'number_of_uses': ('django.db.models.fields.IntegerField', [], {}),
            'type_of_image': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['computing']
