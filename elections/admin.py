from django.contrib import admin
from .models import Election, Candidate

# Inline: allow adding candidates directly in the election form
class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1  # number of blank forms shown

@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_active')  # use your actual field names
    search_fields = ('title',)
    inlines = [CandidateInline]

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'party', 'election')
    search_fields = ('name', 'party')
