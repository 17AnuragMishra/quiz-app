from django.contrib import admin

# Register your models here.
from .models import Question, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # Show 4 option fields at once

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Question, QuestionAdmin)