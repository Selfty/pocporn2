from django.contrib import admin
from .models import Epizoda, Serial, Topserials

class EpizodaAdmin(admin.ModelAdmin):
    list_display = ('epizoda_serial','cislo_serie','cislo_epizoda')
    list_select_related = ('epizoda_serial',)
    pass

admin.site.register(Epizoda, EpizodaAdmin)

class SerialAdmin(admin.ModelAdmin):
    list_display = ('title_cz',)
    pass

admin.site.register(Topserials)

admin.site.register(Serial, SerialAdmin)

