import imp
from django.contrib import admin
from . models import *
# Register your models here.


admin.site.register(Product)
admin.site.register(Order_item)
admin.site.register(Order)
admin.site.register(BillingAddress)
admin.site.register(Payment)




admin.site.site_header  =  "Krafta"  
admin.site.site_title =  "Krafta Web Builder" 
admin.site.index_title  = "Krafta Web Builder" 
# admin.site.index_template = "index"