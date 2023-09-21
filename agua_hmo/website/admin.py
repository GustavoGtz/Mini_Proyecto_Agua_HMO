from django.contrib import admin
from .models import Users, Concepts, Debt

# Register your models here.

admin.site.register(Users)
admin.site.register(Concepts)
admin.site.register(Debt)

