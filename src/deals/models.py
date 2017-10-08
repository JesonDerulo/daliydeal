from django.db import models

import datetime
# Create your models here.

class DealManager(models.Manager):
    def active(self):
        return super(DealManager, self).\
            filter(active=True).\
            filter(expire_date__gt=datetime.datetime.now()).\
            order_by("expire_date")

class Deal(models.Model):
    title        = models.CharField(max_length=120)
    description  = models.CharField(max_length=500, null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    expire_date  = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    active       = models.BooleanField(default=True)

    objects = DealManager()


    def __str__(self):
        return self.title
