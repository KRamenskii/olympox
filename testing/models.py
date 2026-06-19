from django.db import models


class Category(models.Model):
    title = models.CharField('Предмет тестирования', max_length=255)

    class Meta:
        verbose_name = 'Предмет тестирования'
        verbose_name_plural = 'Предметы тестирования'
        ordering = ['title']

    def __str__(self):
        return self.title


class Ticket(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name='Предмет тестирования'
    )
    number = models.PositiveIntegerField('Номер билета')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        ordering = ['category', 'number']
        constraints = [
            models.UniqueConstraint(
                fields=['category', 'number'],
                name='unique_ticket_number_in_category'
            )
        ]

    def __str__(self):
        return f'{self.category} — Билет №{self.number}'


class Question(models.Model):
    text = models.TextField('Текст вопроса', unique=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['id']

    def __str__(self):
        return self.text[:80]


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос'
    )
    text = models.TextField('Текст ответа')
    is_correct = models.BooleanField('Правильный ответ', default=False)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['question', 'text'],
                name='unique_answer_text_in_question'
            )
        ]

    def __str__(self):
        return self.text[:80]


class TicketQuestion(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='ticket_questions',
        verbose_name='Билет'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='ticket_questions',
        verbose_name='Вопрос'
    )
    order = models.PositiveIntegerField('Порядок вопроса в билете')

    class Meta:
        verbose_name = 'Вопрос в билете'
        verbose_name_plural = 'Вопросы в билетах'
        ordering = ['ticket', 'order']
        constraints = [
            models.UniqueConstraint(
                fields=['ticket', 'question'],
                name='unique_question_in_ticket'
            ),
            models.UniqueConstraint(
                fields=['ticket', 'order'],
                name='unique_question_order_in_ticket'
            )
        ]

    def __str__(self):
        return f'{self.ticket} — вопрос №{self.order}'