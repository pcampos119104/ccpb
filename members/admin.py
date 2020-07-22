from django.contrib import admin

from members.models import Member, Phone, Minister

admin.site.register(Member)
admin.site.register(Phone)
admin.site.register(Minister)

