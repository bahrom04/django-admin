from django.contrib import admin
from .models import Region, District

# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_filter = ["title"]
    list_editable = ["title"]
    search_fields = ["title"]
    

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class DistrictAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_filter = ["title"]
    list_editable = ["title"]
    search_fields = ["title"]

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"


admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)