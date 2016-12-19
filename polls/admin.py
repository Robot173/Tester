from django.contrib import admin
from polls.models import Question, Experiment, User
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name_question', 'correct')
    list_filter = ('correct', 'name_question')

class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('question_id','user_id', 'answer', 'adequacy', 'time_start')
    list_filter = ('question_id', 'user_id')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(User)