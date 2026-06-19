from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from testing.models import Category


@login_required
def home(request):
    categories = Category.objects.all()

    selected_category_id = request.GET.get('category')

    if selected_category_id:
        selected_category = get_object_or_404(Category, id=selected_category_id)
    else:
        selected_category = categories.first()

    tickets = []

    if selected_category:
        tickets = (
            selected_category.tickets
            .annotate(
                question_count=Count(
                    'ticket_questions',
                    distinct=True
                ),
                correct_question_count=Count(
                    'ticket_questions__question',
                    filter=Q(ticket_questions__question__answers__is_correct=True),
                    distinct=True
                )
            )
            .order_by('number')
        )

    context = {
        'categories': categories,
        'selected_category': selected_category,
        'tickets': tickets,
    }

    return render(request, 'core/home.html', context)