from django.contrib import admin

# Register your models here.
from .models import Parties,Mumbai_Region,Candidate

class CandidateInline(admin.TabularInline):
    model = Candidate   
    extra = 1

class MumbaiRegion(admin.ModelAdmin):
    list_display = ('assembly_constitution_name','distric')
    inlines = [CandidateInline]
    

class PartiesModel(admin.ModelAdmin):
    list_display = ('party_name','current_leader')
    inlines = [CandidateInline]


admin.site.register(Parties, PartiesModel)
admin.site.register(Mumbai_Region, MumbaiRegion)



# admin.site.register(Parties)
# admin.site.register(Mumbai_Region)
# admin.site.register(Candidate)
