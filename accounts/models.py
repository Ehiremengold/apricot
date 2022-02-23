from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.utils.crypto import get_random_string
from datetime import datetime
User = settings.AUTH_USER_MODEL 
import random
import string

class MyAccountManager(BaseUserManager):

	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address.')
		if not username:
			raise ValueError('Users must have a username.')

		user = self.model(email=self.normalize_email(email),
						username=username,)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			username=username,
			password=password,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user



class Account(AbstractBaseUser):
	email = models.EmailField(verbose_name='email', unique=True, max_length=100)
	username = models.CharField(verbose_name='username', unique=True, max_length=30)
	date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
	last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	objects = MyAccountManager()

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['username']

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True 



# def GetTagId(length):
# 	tag_characters = 'abcdeNOPQRSTUfghirstuvwxyz0123ABCDjklmnopqEFGHIJKL456x9MVWXYZ'
# 	return ''.join(random.choice(tag_characters) for i in range(length))

# CHOICES = (('NGN', 'NGN'),
# 			('USD', 'USD'))

chars = 'abcdeNOPQRSTUfghirstuvwxyz0123ABCDjklmnopqEFGHIJKL456x9MVWXYZ' 

def unique_rand():
	while True:
		wallet_tag = get_random_string(16, chars.lower())
		if not Dashboard.objects.filter(wallet_tag=wallet_tag).exists():
			return wallet_tag

class Dashboard(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# wallet_balance = models.DecimalField(default=0.00, decimal_places=2, max_digits=300)
	wallet_balance = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
	wallet_tag = models.CharField(default=unique_rand, unique=True, max_length=16)
	# bvn = models.CharField(unique=True, max_length=11)
	# accountnumber = models.CharField(max_length=10)
	# accountname = models.CharField(max_length=50)
	# bank = models.CharField(max_length=30)
	# currency = models.CharField(max_length=3, choices=CHOICES, default='NGN')


	def __str__(self):
		return f'{self.user.username}\'s Dashboard'

	
class TransactionRecord(models.Model):
	sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
	receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
	amount = models.DecimalField(decimal_places=2, max_digits=10)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.amount}'

# possible attributes of this model?
# owner, price, name, description, thumbnail

# class Services(models.Model):
# 	owner = models.ForeignKey(User, on_delete=models.CASCADE)
# 	price = models.IntegerField()
# 	description = models.CharField(max_length=200)
# 	thumbnail = models.ImageField(upload_to=f'{self.owner.username}\' service_thumbnail')

class Product(models.Model):
	pass

