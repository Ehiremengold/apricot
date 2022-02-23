import decimal
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (AccountSerializer, 
							DashboardSerializer, 
							TransactionRecordSerializer,
							RegisterSerializer,
							LoginSerializer)
from accounts.models import (Account, 
							Dashboard, 
							TransactionRecord)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django.db.models import Q
# from django.contrib.auth import get_user_model
# from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView 
# User =  get_user_model
# from knox.auth import AuthToken
# ACCOUNT, DASHBOARD, TRANSACTIONRECORD apis

# chars = 'abc456789deNOPQRSTUfghirstuvwxyz0123ABCDjklmnopqEFGHIJKL456x9MVWXYZ'

class RegisterView(generics.GenericAPIView):
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		password = request.data.get('password')
		password2 = request.data.get('password2')
		if password != password2:
			return Response('Passwords don\'t match, Try again!')
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response({
			"user": AccountSerializer(user, context=self.get_serializer_context()).data,
			"token": AuthToken.objects.create(user)[1]
		})


class DashboardView(APIView):
	
	def get(self, request):
		user = request.user
		try:
			user_dashboard = Dashboard.objects.get(user=user)
		except Dashboard.DoesNotExist:
			return Response(serializer.error)
		serializer = DashboardSerializer(user_dashboard)
		filter_backends = DjangoFilterBackend
		permission_classes = [IsAuthenticated]
		return Response(serializer.data)

class TransactionsView(APIView):

	def get(self, request):
		user = request.user
		try:
			user_transaction = TransactionRecord.objects.filter(Q(sender=user) | Q(receiver=user)).order_by('-timestamp')
		except TransactionRecord.DoesNotExist:
			return Response(serializer.errors)
		permission_classes = [IsAuthenticated]
		serializer = TransactionRecordSerializer(user_transaction, many=True)
		return Response(serializer.data)



# sender: request.user, receiver: get_user by (tag, email or id), amount: $20
# receiver.dashboard.wallet_balance
# sender.dashboard.wallet_balance
# increment with amount on receiver end
# decrement with amount on sender end
# create transaction record.

class TransferWithEmailView(APIView):

	def post(self, request, *args, **kwargs):

		sender = Dashboard.objects.get(user=request.user)
		receiving_user = request.data.get('email')
		receiver = Dashboard.objects.get(user__email=receiving_user)
		amount = request.data.get('amount')

		if sender.wallet_balance > decimal.Decimal(amount):
			sender.wallet_balance -= decimal.Decimal(amount)
			sender.save()

			receiver.wallet_balance += decimal.Decimal(amount)
			receiver.save()

			TransactionRecord.objects.create(sender=sender.user, receiver=receiver.user, amount=str(amount))
			return Response('success', status=status.HTTP_200_OK)
		else:
			return Response("Insufficient funds", status=status.HTTP_406_NOT_ACCEPTABLE)


# this works but its sending to a user id
# above code will try to send to an actual tag/email
class TransferView(APIView):

	def post(self, request, *args, **kwargs):

		sender = Dashboard.objects.get(user=request.user)
		receiving_user = request.data.get('receiver')
		receiver = Dashboard.objects.get(user__id=receiving_user)
		amount = request.data.get('amount')

		
		if sender.wallet_balance > decimal.Decimal(amount):
			sender.wallet_balance -= decimal.Decimal(amount)
			sender.save()

			receiver.wallet_balance += decimal.Decimal(amount)
			receiver.save()
			
			TransactionRecord.objects.create(sender=sender.user, receiver=receiver.user, amount=str(amount))
			return Response("success", status=status.HTTP_200_OK)
		else:
			return Response('Insufficient funds', status=status.HTTP_406_NOT_ACCEPTABLE)


class TransferWithTagView(APIView):

	def post(self, request, *args, **kwargs):

		sender = Dashboard.objects.get(user=request.user)
		receiving_user_tag = request.data.get('tag')
		receiver = Dashboard.objects.get(wallet_tag=receiving_user_tag)
		amount = request.data.get('amount')

		if sender.wallet_balance > decimal.Decimal(amount):
			sender.wallet_balance -= decimal.Decimal(amount)
			sender.save()

			receiver.wallet_balance += decimal.Decimal(amount)
			receiver.save()

			TransactionRecord.objects.create(sender=sender.user, receiver=receiver.user, amount=str(amount))
			return Response('success', status=status.HTTP_200_OK)
		else:
			return Response("Insufficient funds", status=status.HTTP_406_NOT_ACCEPTABLE)