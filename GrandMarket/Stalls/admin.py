from django.contrib import admin
from oscar.core.loading import get_model

Stall = get_model('Stalls', 'Stall')
StallStock = get_model('Stalls', 'StallStock')


class StallAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stall, StallAdmin)
admin.site.register(StallStock, StallAdmin)
