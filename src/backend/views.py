from flask import request, Blueprint, render_template
import pickle
from .textCleanFuncs import convert_lower, remove_special, remove_stopwords, stem_words, join_back
import os
import sklearn
filename = '/backend/ImpactHacksModel.pkl'
views = Blueprint('views', __name__)


def cleanText(text):
    text = convert_lower(text)
    text = remove_special(text)
    text = remove_stopwords(text)
    text = stem_words(text)
    text = join_back(text)
    text = [text]
    return text


@views.route('/', methods=['GET', 'POST'])
def run_model():
    if request.method == "POST":
        with open(os.getcwd()+filename, 'rb') as f:
            cv, clf = pickle.load(f)
        text = request.get_json()["formValue"]
        text = cleanText(text)
        text = cv.transform(text).toarray()
        prediction = clf.predict(text)
        prediction = prediction.tolist()
        return {"Prediction": prediction[0]}
    return render_template("base.html")
