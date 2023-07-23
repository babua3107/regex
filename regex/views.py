
import re
from django.shortcuts import render


def regex_query_tool(request):
    input_text = request.GET.get('input_text', '')
    regex_pattern = request.GET.get('regex_pattern', '')
    matched_patterns = []

    if input_text and regex_pattern:
        try:
            regex = re.compile(regex_pattern)
            matched_patterns = regex.findall(input_text)
        except re.error:
            matched_patterns = ["Invalid Regular Expression"]
    

    return render(request, 'query_tool.html', {
        'input_text': input_text,
        'regex_pattern': regex_pattern,
        'matched_patterns': matched_patterns,
    })
