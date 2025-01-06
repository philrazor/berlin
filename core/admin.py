from django.contrib import admin
from .models import Make, CarModel, Part, PartImage

@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make')
    search_fields = ('name', 'make__name')
    list_filter = ('make',)

class PartImageInline(admin.TabularInline):  # Or use StackedInline for a vertical layout
    model = PartImage
    extra = 1  # Number of empty image fields to display


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_model', 'price', 'year', 'engine_code', 'engine_capacity', 'condition')
    search_fields = ('name', 'car_model__name', 'car_model__make__name', 'engine_code')
    list_filter = ('car_model__make', 'car_model', 'condition', 'year')
    inlines = [PartImageInline]