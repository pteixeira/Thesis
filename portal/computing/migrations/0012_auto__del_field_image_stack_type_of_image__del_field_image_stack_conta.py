# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Image_Stack.type_of_image'
        db.delete_column('computing_image_stack', 'type_of_image')

        # Deleting field 'Image_Stack.container_format'
        db.delete_column('computing_image_stack', 'container_format')

        # Deleting field 'Image_Stack.ramdisk_id'
        db.delete_column('computing_image_stack', 'ramdisk_id')

        # Deleting field 'Image_Stack.size'
        db.delete_column('computing_image_stack', 'size')

        # Deleting field 'Image_Stack.disk_format'
        db.delete_column('computing_image_stack', 'disk_format')

        # Deleting field 'Image_Stack.kernel_id'
        db.delete_column('computing_image_stack', 'kernel_id')

        # Deleting field 'Image_Stack.image_status'
        db.delete_column('computing_image_stack', 'image_status')

        # Deleting field 'Image_Stack.architecture'
        db.delete_column('computing_image_stack', 'architecture')

        # Adding field 'Image_Stack.status'
        db.add_column('computing_image_stack', 'status', self.gf('django.db.models.fields.CharField')(max_length=500, null=True), keep_default=False)

        # Adding field 'Image_Stack.description'
        db.add_column('computing_image_stack', 'description', self.gf('django.db.models.fields.CharField')(max_length=500, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Image_Stack.type_of_image'
        db.add_column('computing_image_stack', 'type_of_image', self.gf('django.db.models.fields.CharField')(default=1, max_length=10), keep_default=False)

        # Adding field 'Image_Stack.container_format'
        db.add_column('computing_image_stack', 'container_format', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Image_Stack.ramdisk_id'
        db.add_column('computing_image_stack', 'ramdisk_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Image_Stack.size'
        db.add_column('computing_image_stack', 'size', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Image_Stack.disk_format'
        db.add_column('computing_image_stack', 'disk_format', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Image_Stack.kernel_id'
        db.add_column('computing_image_stack', 'kernel_id', self.gf('django.db.models.fields.CharField')(max_length=500, null=True), keep_default=False)

        # Adding field 'Image_Stack.image_status'
        db.add_column('computing_image_stack', 'image_status', self.gf('django.db.models.fields.CharField')(max_length=100, null=True), keep_default=False)

        # Adding field 'Image_Stack.architecture'
        db.add_column('computing_image_stack', 'architecture', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Deleting field 'Image_Stack.status'
        db.delete_column('computing_image_stack', 'status')

        # Deleting field 'Image_Stack.description'
        db.delete_column('computing_image_stack', 'description')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
            'disk_format': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['computing.Image']"}),
            'image_status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'kernel_id': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ramdisk_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'computing.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'number_of_uses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'type_of_image': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'computing.image_stack': {
            'Meta': {'object_name': 'Image_Stack'},
            'abaqus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ansys': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_last_used': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'gcc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gromacs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matlab': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'number_of_uses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'octave': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'openfoam': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'r': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'user_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'vim': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'computing.tag_search_frequency': {
            'Meta': {'object_name': 'Tag_Search_Frequency'},
            'freq': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        },
        'computing.usage': {
            'Meta': {'object_name': 'Usage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['computing.Image_Stack']"}),
            'number_of_uses': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'computing.user_tasks': {
            'Meta': {'object_name': 'User_Tasks'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['computing']
