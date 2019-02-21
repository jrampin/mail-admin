from django.contrib import admin
from .models import Email,Domain,Alias

class PageDomain(admin.ModelAdmin):
    list_display = ['name','accounts']
    search_fields = ['name']

    def accounts (self, domain):
      return Email.objects.filter(domain__name=domain).count()

class PageAlias(admin.ModelAdmin):
    list_display = ['source','destination']
    search_fields = ['source','destination']

class PageEmail(admin.ModelAdmin):
    list_display = ['email','password', 'aliases', 'lastlogin']
    search_fields = ['email']

    def aliases (self, alias):
      return Alias.objects.filter(destination=alias).count()

admin.site.register(Domain, PageDomain)
admin.site.register(Email, PageEmail)
admin.site.register(Alias, PageAlias)
