from django.contrib import admin

from shortner.models import URL
from shortner.models import ClickEvent

# Register your models here.
admin.site.register(URL)
admin.site.register(ClickEvent)