from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.paginator import Paginator
from django.core.cache import cache
from accounts.models import Account, Dashboard, TransactionRecord

class TransactionRecordAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'amount', 'timestamp')
    search_fields = ('sender', 'amount', 'receiever')
    readonly_fields = ('sender', 'receiver', 'amount')

admin.site.register(TransactionRecord, TransactionRecordAdmin)


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = () 
    fieldsets = ()

"""caches the database incase we have million of messages because it will take a long time to load"""
# Resource: http://masnun.rocks/2017/03/20/django-admin-expensive-count-all-queries/
class CachingPaginator(Paginator):
    def _get_count(self):

        if not hasattr(self, "_count"):
            self._count = None

        if self._count is None:
            try:
                key = "adm:{0}:count".format(hash(self.object_list.query.__str__()))
                self._count = cache.get(key, -1)
                if self._count == -1:
                    self._count = super().count
                    cache.set(key, self._count, 3600)

            except:
                self._count = len(self.object_list)
        return self._count

    count = property(_get_count)


admin.site.register(Account, AccountAdmin)

class DashboardAdmin(admin.ModelAdmin):
	list_display = ('user', 'wallet_tag', 'wallet_balance')
	search_fields = ('user', )
	readonly_fields = ('user', 'wallet_balance', 'wallet_tag')

admin.site.register(Dashboard, DashboardAdmin)
