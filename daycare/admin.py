from django.contrib import admin
from . models import Sitter, Baby, Payment, Procurement


admin.site.register(Sitter)
admin.site.register(Baby)
admin.site.register(Payment)
admin.site.register(Procurement)
