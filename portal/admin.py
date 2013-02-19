from django.contrib import admin
from models import *

class sponsorAdmin(admin.ModelAdmin):
	list_display = ('by'), 

class faqAdmin(admin.ModelAdmin):
	list_dispay = ('question'), ('answer')
	
class penginapanAdmin(admin.ModelAdmin):
	list_display = ("penginapan"),
		

class jadwalAdmin(admin.ModelAdmin):
	list_display = ("kegiatan"),

class informasiAdmin(admin.ModelAdmin):
	list_display = ("informasi"),	
	
admin.site.register(faq, faqAdmin)	
admin.site.register(sponsor_and_partner, sponsorAdmin)
admin.site.register(penginapan, penginapanAdmin)
admin.site.register(jadwal, jadwalAdmin)
admin.site.register(informasi, informasiAdmin)
