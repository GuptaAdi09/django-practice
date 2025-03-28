from django.contrib import admin

# Register your models here.
from .models import Articles

class ArticelsModel(admin.ModelAdmin):
    list_display = ('id','name','author')
    search_fields = ('name',)
    # list_filter = ('name',)

admin.site.register(Articles,ArticelsModel)