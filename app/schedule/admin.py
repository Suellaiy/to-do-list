from django.contrib import admin

from schedule.models import Schedule


@admin.register(Schedule)
class Schedule(admin.ModelAdmin):
    pass
