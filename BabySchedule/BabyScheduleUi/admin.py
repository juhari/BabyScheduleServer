from BabyScheduleUi import models
from django.contrib import admin

class ActivityInline(admin.StackedInline):
    model = models.Activity
    extra = 3

class FamilyAdmin(admin.ModelAdmin):
    fieldset = [(None, {'fields': ['name']})]
    inlines = [ActivityInline]
    
admin.site.register(models.Family, FamilyAdmin)


admin.site.register(models.Baby)
admin.site.register(models.Activity)
admin.site.register(models.BabyEvent)
admin.site.register(models.ActivityParameter)
admin.site.register(models.EventData)