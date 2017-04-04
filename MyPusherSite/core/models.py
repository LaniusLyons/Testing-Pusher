from django.db import models
from django.contrib.auth.models import User as Usuario
import time
import hashlib
import string
import random

def salt_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

def generate_hash():
	hash = hashlib.sha1()
	hash.update(str(time.time()).encode('utf-8')+salt_generator())
	hashfinal = hash.hexdigest()[:-10]
	return hashfinal

def generate_slug():
	return generate_hash()[:12]


class Perfil(Usuario):

	class Meta:
		proxy = True

	CUSTOMER  = 'Us' 
	ADMINISTRATOR = 'Ad'
	GUARD = 'Gd'

	CUSTOMER_T = (
		(CUSTOMER, 'Usuario'),
		(ADMINISTRATOR, 'Administrador'),
		(GUARD, 'Guardia'),
	)

	slug = models.SlugField(unique=True,default=generate_slug)
	fk_universidad = models.ForeignKey('Universidad',blank=True,null=True,related_name='universidad')
	type = models.CharField(max_length=2, choices=CUSTOMER_T,default='Us')


	class Meta:
		db_table = 'Perfil'

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
