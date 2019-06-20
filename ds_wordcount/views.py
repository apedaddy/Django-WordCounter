from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictonary = {}
    for word in wordlist:
        if word in worddictonary:
            #add each word
            worddictonary[word] += 1
        else:
            #add to dict
            worddictonary[word]=1
    sorted_wordlist = sorted(worddictonary.items(), key=operator.itemgetter(1), reverse=True)

    highestoccurance = (sorted_wordlist [0][0])

    totaloccurance = (sorted_wordlist [0][1])

    return render(request, 'count.html',{'fulltext':fulltext,'count': len(wordlist), 'countall': sorted_wordlist, 'highest':highestoccurance, 'maxno': totaloccurance})

    #return highestoccurance, totaloccurance