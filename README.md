# News Headline Keyword Extractor

## Overview

News Headline Keyword Extractor is a Flask-based Natural Language Processing (NLP) web application that extracts meaningful root keywords from a news headline.

The application performs:

* Tokenization
* Stopword Removal
* Stemming
* Root Keyword Extraction

Users can enter a news headline and instantly view the extracted root keywords.

---

## Features

* Extracts keywords from news headlines
* Removes common English stopwords
* Applies Porter Stemming Algorithm
* Simple and responsive user interface
* Built using Flask and NLTK
* Deployed on Vercel

---

## Technologies Used

* Python
* Flask
* NLTK
* HTML
* CSS
* Vercel

---

## Project Structure

```text
Internship-Project/
│
├── nltk_data/
│   ├── corpora/
│   └── tokenizers/
│
├── templates/
│   └── index.html
│
├── main.py
├── requirements.txt
├── vercel.json
└── README.md
```

---

## How It Works

1. User enters a news headline.
2. The headline is tokenized into individual words.
3. Stopwords are removed.
4. Remaining words are stemmed using Porter Stemmer.
5. Root keywords are displayed to the user.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd Internship-Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Live Demo

Deployed Application:

[Add Your Vercel URL Here]

---

## Sample Input

```text
Scientists discover new technologies for improving healthcare systems
```

## Sample Output

```text
scientist
discover
technolog
improv
healthcar
system
```

---

## Future Enhancements

* Lemmatization support
* Keyword frequency analysis
* Named Entity Recognition (NER)
* Support for multiple headlines
* Export extracted keywords

---

## Author

Developed as part of an NLP internship project using Flask and NLTK.
