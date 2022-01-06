from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from itertools import islice

list_to_remove = ["ile", "ve", "veya", "ki", "de", "da", "ama", "eğer", "hem", "yani", "öyleyse", "yoksa",
                      "nitekim", "sanki", "kim", "ya", "ne", "hem", "ama", "mesela", "üstelik", "bu", "şu", "o"
                      "âdeta","ancak", "bari", "belki", "binaenaleyh", "çünkü", "eğer", "fakat", "gerçi", "güya", "hakeza",
                      "hâlbuki", "hatta", "hazır", "hele", "illâ", "keşke", "keza", "lâkin", "madem",
                      "mademki", "mamafih", "meğerki", "nasıl", "nitekim", "oysaki", "öyle", "sanki", "şayet", "şöyle",
                      "tâ", "üstelik", "yalnız", "yani", "yoksa", "zaten", "zati", "gibi", "ancak", "başka",
                      "beri", "bir", "tek", "dair", "değil", "değin", "denli", "dek", "dolayı", "diye", "evvel",
                      "gayri", "gibi", "göre", "için", "ile", "kadar", "karşı", "karşın", "mukabil", "önce", "ötürü",
                      "öte", "rağmen", "sadece", "sanki", "sonra", "sıra", "üzere", "yalnız", "olarak", "şimdi", "daha",
                      "burda", "burada", "şurda", "şurada", "orda", "orada", "ben", "sen", "o", "biz", "siz",
                      "onlar", "bunlar", "şunlar", "bir", "sonra", "ise", "olan"]

def process(iterable):
    remove = []
    for x in iterable:
        if x[0] in list_to_remove:
            remove.append(x)
    processed = [x for x in iterable if x not in remove]
    return processed

def take(n, iterable):
    return list(islice(iterable, n))

def getNum(iterable):
    words_used = int((len(set(iterable))))
    if words_used < 5000:
        return 5
    else:
        return (int(words_used/1000))

def getContent1(url):
    req1 = requests.get(url)
    soup = BeautifulSoup(req1.content, "lxml")
    text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    word_list = c.most_common()
    processed_list = process(word_list)
    n = getNum(processed_list)
    most_c = take(n, processed_list)
    return (most_c)

def getContent2(url):
    req2 = requests.get(url)
    soup = BeautifulSoup(req2.content, "lxml")
    text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    word_list = c.most_common()
    processed_list = process(word_list)
    n = getNum(processed_list)
    most_c = take(n, processed_list)
    return (most_c)

def getWordList(url):
    r_word = requests.get(url)
    soup = BeautifulSoup(r_word.content, "lxml")
    text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    word_list = c.most_common()
    return (word_list)

def calcScore(iter1, iter2):
    total = 0
    same_word_freq = 0

    for x in iter1:
        total = total + int(x[1])

    for x in iter1:
        for y in iter2:
            if x[0] == y[0]:
                same_word_freq = same_word_freq + int(x[1])

    return int((same_word_freq*100)/total)

# Create your views here.
def home(request):
    freq1 = None
    freq2 = None
    score12 = None
    score21 = None
    if "url_to_scrape1" in request.GET and "url_to_scrape2" in request.GET:
        uTs1 = request.GET.get("url_to_scrape1")
        freq1 = getContent1(uTs1)
        wl1 = process(getWordList(uTs1))
        uTs2 = request.GET.get("url_to_scrape2")
        freq2 = getContent2(uTs2)
        wl2 = process(getWordList(uTs2))
        score12 = calcScore(wl1, wl2)
        score21 = calcScore(wl2, wl1)

    return render(request, "asama23/home.html", {"frequencies1": freq1, "frequencies2": freq2, "score12": score12, "score21": score21})
