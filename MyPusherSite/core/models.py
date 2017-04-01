from django.db import models
from django.contrib.auth.models import User as Usuario
import time
import hashlib

def generate_hash():
	hash = hashlib.sha1()
	hash.update(str(time.time()).encode('utf-8')+salt_generator())
	hashfinal = hash.hexdigest()[:-10]
	return hashfinal

def generate_slug():
	return generate_hash()[:12]

# Create your models here.

class Universidad(models.Model):
	id = models.AutoField(primary_key=True)
	slug = models.SlugField(unique=True,default=generate_slug)
	nombre = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	aprobado = models.BooleanField(default=False)

	class Meta:
		db_table = 'Universidad'

	def __unicode__(self):
		return self.nombre
	

class Companero(models.Model):
	id = models.AutoField(primary_key=True)
	slug = models.SlugField(unique=True,default=generate_slug)
	id_usuario_uno = models.ForeignKey(Usuario, related_name='usuario')
	id_usuario_dos = models.ForeignKey(Usuario, related_name='companero')
	id_universidad = models.ForeignKey(Universidad)

	class Meta:
		db_table = 'Companero'
