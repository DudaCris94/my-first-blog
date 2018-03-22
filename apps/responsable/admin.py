# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib import admin

# Register your models here.
from apps.responsable.models import Responsable

admin.site.register(Responsable)