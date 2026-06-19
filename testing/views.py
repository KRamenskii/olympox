from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render

from .models import Ticket


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(
        Ticket.objects.select_related('category'),
        id=ticket_id
    )

    ticket_questions = list(
        ticket.ticket_questions
        .select_related('question')
        .prefetch_related('question__answers')
        .order_by('order')
    )

    correct_questions = 0

    for item in ticket_questions:
        item.has_correct_answer = item.question.answers.filter(is_correct=True).exists()

        if item.has_correct_answer:
            correct_questions += 1

    total_questions = len(ticket_questions)

    context = {
        'ticket': ticket,
        'ticket_questions': ticket_questions,
        'total_questions': total_questions,
        'correct_questions': correct_questions,
    }

    return render(request, 'testing/ticket_detail.html', context)