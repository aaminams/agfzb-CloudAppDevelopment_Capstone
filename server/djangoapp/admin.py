from django.contrib import admin
from .models import CarMake,CarModel


class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name','desc','brand']
    inlines = [CarModelInline]
class CarModelAdmin(admin.ModelAdmin):
    fields = ['dealer_id','name','car_type','year','color']

admin.site.register(CarMake,CarMakeAdmin)
admin.site.register(CarModel,CarModelAdmin)
