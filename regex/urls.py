
from django.urls import path
from regex.views import regex_query_tool

urlpatterns = [
    path('', regex_query_tool, name='regex_query_tool'),
]
