from django.contrib import admin
from .models import Contact, FabricRoll, Cutting, Ironing, Sewing

admin.site.register(Contact)
admin.site.register(FabricRoll)
admin.site.register(Cutting)
admin.site.register(Ironing)
admin.site.register(Sewing)
