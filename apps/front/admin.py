from django.contrib import admin
from apps.front import models

class QuoteAdmin(admin.ModelAdmin):
    list_filter = ('author', 'lecturer')

class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description')

admin.site.register(models.Lecturer)
admin.site.register(models.LecturerRating)
admin.site.register(models.Quote, QuoteAdmin)
admin.site.register(models.Document)
admin.site.register(models.DocumentCategory, DocumentCategoryAdmin)
admin.site.register(models.DocumentRating)
admin.site.register(models.Event)
