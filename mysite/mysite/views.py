from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def text_analysis(request):
    django_text=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    fullsmall=request.POST.get('fullsmall','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    wordcounter=request.POST.get('wordcounter','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in django_text:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        django_text=analyzed
    if fullcaps == "on":
        analyzed=""
        for char in django_text:
            analyzed+=char.upper()
        params={'purpose':'Changed to UPPERCASE','analyzed_text':analyzed}
        django_text=analyzed
    if fullsmall == "on":
        analyzed=""
        for char in django_text:
            analyzed+=char.lower()
        params={'purpose':'Changed to lowercase','analyzed_text':analyzed}
        django_text=analyzed
    if newlineremover == 'on':
        analyzed=""
        for char in django_text:
            if char!="\n" and char!='\r':
                analyzed+=char
        params={'purpose':'Removed New Lines','analyzed_text':analyzed}
        django_text=analyzed
    if extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate(django_text):
            if not (django_text[index]==' ' and django_text[index+1]==' '):
                analyzed+=char
        params={'purpose':'Removed Extra Spaces','analyzed_text':analyzed}
        django_text=analyzed
    if charcounter=='on' and wordcounter=='on':
        return HttpResponse("<h1>Please select only one operation at a time from Count the number of characters & Count the number of words then try again!</h1>")    
    if charcounter=='on':
        analyzed=0
        for char in django_text:
            analyzed+=1
        res=(f'The number of characters in {django_text} is {analyzed} characters.')
        params={'purpose':'Character Counter','analyzed_text':res}
        django_text=analyzed
    if wordcounter=='on':
        analyzed=0
        for word in django_text.split():
            analyzed+=1
        res=(f'The number of words in {django_text} is {analyzed} words.')
        params={'purpose':'Word Counter','analyzed_text':res}
        django_text=analyzed    
    
    if removepunc!="on" and fullcaps!="on" and fullsmall!='on' and newlineremover!='on' and extraspaceremover!='on' and charcounter!='on' and wordcounter!='on':
        return HttpResponse("<h1>Please select any operation and try again!</h1>")
    return render(request,"analyze.html",params)

