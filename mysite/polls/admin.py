from django.contrib import admin
<<<<<<< HEAD
from .models import Question,Choice

# Register your models here

class ChoiceInline(admin.StackedInline):
=======

# Register your models here.
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):

>>>>>>> 201094cea5538c2ff459630ce6e1396813bee7fd
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
=======
    list_display = ('question_text', 'pub_date','was_published_recently')
    inlines = [ChoiceInline]
>>>>>>> 201094cea5538c2ff459630ce6e1396813bee7fd
    list_filter = ['pub_date']
    search_fields = ['question_text']


<<<<<<< HEAD
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
=======

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
>>>>>>> 201094cea5538c2ff459630ce6e1396813bee7fd
