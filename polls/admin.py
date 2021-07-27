from django.contrib import admin
from .models import Question, Choice

class  QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields' : ['question_text']}),
        ('Date information', {'fields' : ['pud_date']}),
    ]
    # fields = ['pud_date','question_text']


admin.site.register(Question)
admin.site.register(Choice)

