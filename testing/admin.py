from django.contrib import admin
from .models import Category, Ticket, Question, Answer, TicketQuestion


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class TicketQuestionInline(admin.TabularInline):
    model = TicketQuestion
    extra = 1
    autocomplete_fields = ['question']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'number']
    list_filter = ['category']
    search_fields = ['category__title']
    inlines = [TicketQuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_text']
    search_fields = ['text']
    inlines = [AnswerInline]

    def short_text(self, obj):
        return obj.text[:100]

    short_text.short_description = 'Вопрос'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_text', 'question', 'is_correct']
    list_filter = ['is_correct']
    search_fields = ['text', 'question__text']

    def short_text(self, obj):
        return obj.text[:100]

    short_text.short_description = 'Ответ'


@admin.register(TicketQuestion)
class TicketQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'ticket', 'question', 'order']
    list_filter = ['ticket__category', 'ticket']
    autocomplete_fields = ['ticket', 'question']