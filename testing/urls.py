from django.urls import path

from .views import ticket_detail

app_name = 'testing'

urlpatterns = [
    path('tickets/<int:ticket_id>/', ticket_detail, name='ticket_detail'),
]