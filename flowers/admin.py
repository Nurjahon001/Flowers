from django.contrib import admin
from .models import Flowers, FlowerReview, FlowerDesigner, Designer


# Register your models here.


class FlowerModelAdmin(admin.ModelAdmin):
    search_fields = ['name_f','description','symbolism']
    list_display = ['name_f','symbolism']
    list_filter = ['create_at']


admin.site.register(FlowerDesigner)
admin.site.register(Flowers,FlowerModelAdmin)
admin.site.register(Designer)
admin.site.register(FlowerReview)