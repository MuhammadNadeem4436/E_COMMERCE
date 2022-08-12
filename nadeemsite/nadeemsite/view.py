# Write your view hare

# code for vedio 6:

# from django.http import HttpResponse

# def index(request):
#     # return HttpResponse("hello")
#
# # for adding link of a file.
#         return HttpResponse('''<h1>Hello nadeem</h1> <a href= "https://www.youtube.com/watch?v=
#         AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=9" <a>Django withharry</a>> ''')
#
#
# def about(request):
#     return HttpResponse("About nadeem")

# code for vedio7

# def index(request):
#     return HttpResponse("Home")
#
# def removepunc(request):
#     return HttpResponse("remove punc <a href='/'>back</a>")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")

# CODE FOR TEMPLATES

# from django.http import HttpResponse
# from django.shortcuts import render
#
#
# def removepunc(request):
#     # get the text
#     djtext = print(request.GET.get('text','default'))
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("remove punc <a href='/'>back</a>")
#
# def index(request):
#     # dic = {'name':'Nadeem','Place':'Pakistan'}
#     return render(request, 'index.html')

# CODE FOR BACKEND

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepun','off')
    fullcaps = request.POST.get('fullcaps','off')
    print(removepunc)
    print(djtext)
    # analyzed = djtext
    punctuation = '''!()-[]{}:;'"\,<>./?@#$%&*_-'''
    analyzed = ""
    for char in djtext:
        if char not in punctuation:
            analyzed  = analyzed + char

    params= {'purpose':'RemovePunctuations','analyzed_text':analyzed}
    # Analyze the text
    # return HttpResponse("remove punc <a href='/'>back</a>")
    return render(request, 'analyze.html',params)

    for char in djtext:
        if fullcaps == 'on:':
            analyzed = analyzed + char.upper()

    params = {'purpose':'Change to upper case','analyzed_text':analyzed}

    return render(request, 'analyze.html',params)
