import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from flask import Flask, request, render_template



app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        headline_text = request.form.get("headline_text")
        stemmer = PorterStemmer()
        token = word_tokenize(headline_text)

        stop_words = set(stopwords.words("english"))
        common_symbols = {',', '?', '.', '"', "'", ':', ';', '!', '@', '#', '$', '%', '*', '&', '(', ')'}
        stop_words.update(common_symbols)
        stop_words_list = [words for words in token if words.lower() not in stop_words]
        stemmed_words = [stemmer.stem(words) for words in stop_words_list]
        result = " ".join(stemmed_words)

        return render_template("index.html", result = result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)