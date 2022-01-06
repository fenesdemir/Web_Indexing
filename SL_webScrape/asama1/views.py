from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from itertools import islice


def getContent(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    word_list = c.most_common()
    return (word_list)

# Create your views here.
def home(request):
    freq = None
    if "url_to_scrape" in request.GET:
        uTs = request.GET.get("url_to_scrape")
        freq= getContent(uTs)
    return render(request, "asama1/home.html", {"frequencies": freq})