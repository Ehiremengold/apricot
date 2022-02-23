from rest_framework import serializers, routers, viewsets
from accounts.models import Account, Dashboard, TransactionRecord
from django.conf import settings
User = settings.AUTH_USER_MODEL 

class AccountSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ['email', 'username']

class LoginSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ['email', 'password']

		
class RegisterSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ['email', 'username', 'password']
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validate_data):
		account = Account.objects.create_user(validate_data['email'], validate_data['username'], validate_data['password'])

		return account

class DashboardSerializer(serializers.ModelSerializer):

	class Meta:
		model = Dashboard
		fields = ['user', 'wallet_balance', 'wallet_tag']

class TransactionRecordSerializer(serializers.ModelSerializer):

	class Meta:
		model = TransactionRecord
		fields = ['sender', 'receiver', 'amount', 'timestamp']

