from django.urls import path
from .views import ( DashboardView, 
					TransactionsView,
					TransferView,
					TransferWithEmailView,
					TransferWithTagView,
					RegisterView,
					)


urlpatterns = [
	path('register/', RegisterView.as_view(), name='custom-registration-api'),
	path('dashboard/', DashboardView.as_view(), name='api-dashboard'),
	# path('users/', AccountView.as_view(), name='api-users'),
	path('transactions/', TransactionsView.as_view(), name='api-transactions'),
	path('transfer/', TransferView.as_view(), name='api-transfer'),
	path('transfer/email/', TransferWithEmailView.as_view(), name='api-transfer-email'),
	path('transfer/tag/', TransferWithTagView.as_view(), name='api-transfer-tag'),
]