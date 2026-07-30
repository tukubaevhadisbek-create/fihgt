from django.contrib import admin
from .models import Trenery, Schedule, Price, Contact, Training, Direction


@admin.register(Trenery)
class TreneryAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'name',
        'sport',
        'experiense',
        'description',
    )
    list_display_links = ['name']
    search_fields = ('name', 'sport')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'day',
        'time',
        'group',
    )
    list_display_links = ['day']
    search_fields = ('day', 'group')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'price',
        'bonus1',
        'bonus2',
        'bonus3',
    )
    list_display_links = ['type']
    search_fields = ('type',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'phone',
        'telegram',
        'map',
        'email',
    )
    list_display_links = ['telegram', 'email']
    search_fields = ('telegram', 'email')

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'naprav',
        'description',
    )
    list_display_links = ('name',)
    search_fields = ('name', 'naprav')



@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )