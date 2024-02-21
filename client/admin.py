from django.contrib import admin
from .models import Ticket, Client


admin.site.register([Ticket, Client])