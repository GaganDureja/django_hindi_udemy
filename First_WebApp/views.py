from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):

    return render(request,"index.html",{'key1':'I am coming from python code'})
def result(request):
    text = request.GET['user_text']
    words = text.split()
    word_count = len(words)
    dict_words = {}
    for word in words:
        if(word in dict_words):
            dict_words[word] +=1
        else:
            dict_words[word] = 1
        sort_dict = sorted(dict_words.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,"result.html", {'text':text, 'word_count': word_count,'dict_words':sort_dict})
