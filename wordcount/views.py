from django.http import HttpResponse
from django.shortcuts import render
import operator

'''def home(request):
    #return HttpResponse("Hello") # This will return string
    return render(request, 'home.html', {"hithere":"This is me!"})'''

def home(request):
    return render(request, 'home.html')

def egg(request):
    return HttpResponse('<h1>Egg Shop<h1>')

def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext) # This line will be printed in the cmd line where server is running
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
    return  render(request, "about.html")