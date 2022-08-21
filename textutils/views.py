# I have created this file- Prabal Ghosh

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("<h1>hello prabal</h1>")
    params = {'name': 'prabal', 'place': 'kolkata'}
    my_dict = {'first_name': 'John', 'last_name': 'Doe'}
    # return render(request, 'index.html',params)
    return render(request, 'index.html')

def about(request):
    return HttpResponse('''<h1>1st django app using python by prabal </h1><a href='/'>back</a>''')
def text1(request):
    file_1=open("/Users/pgosh/PycharmProjects/harry-1/textutils/textutils/one.txt",'r')
    content_1=file_1.read()
    file_1.close()
    return HttpResponse(content_1)

def link1(request):
    return HttpResponse('''<h1> Prabal</h1> <a href="https://in.linkedin.com/in/prabal-ghosh-25a196158?original_referer=https%3A%2F%2Fwww.google.com%2F"> LinekdIn</a>''')

# def removepunc(request):
#     #Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove first")


def spaceremove(request):
    return HttpResponse("space remover back")

def charcount(request):
    return HttpResponse("charcount ")


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    # get check bok values
    removepunc=request.GET.get('removepunc','off')
    fullcaps= request.GET.get('fullcaps','off')
    newlineremover= request.GET.get('newlineremover','off')
    extraspaceremover= request.GET.get('extraspaceremover','off')


    # check that the chec k box is on or not
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse('Error')

def ex1(request):
    # s = ''' Navigation Bar <br> </h2>
    #    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    #    <a href="https://www.facebook.com/"> Facebook </a> <br>
    #    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    #    <a href="https://www.hindustantimes.com/"> News </a> <br>
    #    <a href="https://www.google.com/"> Google </a> <br>'''
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    # return HttpResponse(s)
    return HttpResponse(sites)