from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter
def home(request):

    return render(request,"index.html",{'key1':'I am coming from python code'})
def result(request):
    text = request.GET['user_text']
    sort_dict,word_count =counter.count(text)
    return render(request,"result.html", {'text':text, 'word_count': word_count,'dict_words':sort_dict})
