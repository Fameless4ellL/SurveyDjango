from django.contrib import admin
from .models import Question, Choice, Polls, TypeQA, Vote


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['descriptionQA', 'typeQA']}),
    ]
    inlines = [ChoiceInline]


class PollAdmin(admin.ModelAdmin):
    # block s_date after editing
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['s_date']
        return self.readonly_fields


admin.site.register(Question, QuestionAdmin)
admin.site.register(Polls, PollAdmin)
admin.site.register(TypeQA)
admin.site.register(Vote)
