from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")


def text_analysis(request):
    django_text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    fullsmall = request.POST.get('fullsmall', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    titlecase = request.POST.get('titlecase', 'off')
    removedigits = request.POST.get('removedigits', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in django_text:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        django_text = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in django_text:
            analyzed += char.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        django_text = analyzed
    if fullsmall == "on":
        analyzed = ""
        for char in django_text:
            analyzed += char.lower()
        params = {'purpose': 'Changed to lowercase', 'analyzed_text': analyzed}
        django_text = analyzed
    if newlineremover == 'on':
        analyzed = ""
        for char in django_text:
            if char != "\n" and char != '\r':
                analyzed += char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        django_text = analyzed
    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(django_text):
            if not (django_text[index] == ' ' and django_text[index+1] == ' '):
                analyzed += char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        django_text = analyzed
    if titlecase == 'on':
        analyzed = ' '.join([w.capitalize() for w in django_text.split(' ')])
        params = {'purpose': 'Converted to Title Case',
                  'analyzed_text': analyzed}
        django_text = analyzed
    if removedigits == 'on':
        analyzed = ''.join(ch for ch in django_text if not ch.isdigit())
        params = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}
        django_text = analyzed

    if removepunc != "on" and fullcaps != "on" and fullsmall != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and titlecase != 'on' and removedigits != 'on':
        return HttpResponse("<h1>Please select any operation and try again!</h1>")
    return render(request, "analyze.html", params)
