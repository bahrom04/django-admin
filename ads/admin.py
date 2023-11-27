from django.contrib import admin
from .models import Ads, AdsAttributeValue, Category, SubCategory,AdsAttributeValueOption


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Ads)
admin.site.register(AdsAttributeValue)
admin.site.register(AdsAttributeValueOption)
