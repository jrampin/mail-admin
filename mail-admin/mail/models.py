from django.db import models
from passlib.hash import pbkdf2_sha256, sha256_crypt

#
# Domains
#
class Domain(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Domain'
        verbose_name_plural = 'Domains'
        managed = False
        db_table = 'virtual_domains'

    def __str__(self):
        return self.name

#
# Aliases
#
class Alias(models.Model):
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE)
    source =  models.CharField(max_length=100)
    destination =  models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Alias'
        verbose_name_plural = 'Aliases'
        managed = False
        db_table = 'virtual_aliases'

    def __str__(self):
        return self.source

#
# Emails
#
class Email(models.Model):
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=150)
    lastlogin = models.DateTimeField(max_length=50, editable=False)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
        managed = False
        db_table = 'virtual_users'

    def __str__(self):
        return self.email

    def save(self, **kwarg):
        new_password = '{SHA256-CRYPT}' + sha256_crypt.hash(self.password)
        self.password = new_password
        super().save(**kwarg)
