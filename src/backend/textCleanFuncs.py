from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk


def convert_lower(text):
    return text.lower()


def remove_special(text):
    x = ''

    for i in text:
        if i.isalnum():
            x = x+i
        else:
            x = x + ' '
    return x


nltk.download("stopwords")
stop_words = set(stopwords.words('english'))


def remove_stopwords(text):
    x = []
    for i in text.split():
        if i not in stop_words:
            x.append(i)
    y = x[:]
    x.clear()
    return y


ps = PorterStemmer()

y = []


def stem_words(text):
    for i in text:
        y.append(ps.stem(i))
    z = y[:]
    y.clear()
    return z


def join_back(list_input):
    return " ".join(list_input)
