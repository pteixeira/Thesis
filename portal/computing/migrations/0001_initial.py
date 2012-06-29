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
            ('type_of_image', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('number_of_uses', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('computing', ['Image'])

        # Adding model 'Image_Stack'
        db.create_table('computing_image_stack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('user_owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('type_of_image', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('number_of_uses', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('kernel_id', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image_status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ramdisk_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('architecture', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('container_format', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('disk_format', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('vim', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('matlab', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('abaqus', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gcc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('r', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('octave', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gromacs', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('openfoam', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ansys', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('computing', ['Image_Stack'])

        # Adding model 'Details_OpenStack'
        db.create_table('computing_details_openstack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['computing.Image'])),
            ('kernel_id', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
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
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['computing.Image'])),
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

        # Deleting model 'Image_Stack'
        db.delete_table('computing_image_stack')

        # Deleting model 'Details_OpenStack'
        db.delete_table('computing_details_openstack')

        # Deleting model 'Details_OpenNebula'
        db.delete_table('computing_details_opennebula')


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
            'architecture': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'container_format': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'disk_format': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gcc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gromacs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'kernel_id': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'matlab': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'number_of_uses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'octave': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'openfoam': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'r': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ramdisk_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'tags': ('tagging.fields.TagField', [], {}),
            'type_of_image': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'vim': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
