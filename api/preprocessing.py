import re
import string

import contractions
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")


patterns_replacements = {r"c\+\+": "cplusplus", r"c#": "csharp", r"node.js": "nodejs"}


# Perform the replacements
def replace_programming_language_name(input_string):
    output_string = input_string
    for pattern, replacement in patterns_replacements.items():
        output_string = re.sub(pattern, replacement, output_string)

    return output_string


def clean_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    clean_text = soup.get_text()
    return clean_text


def clean_newlines(text):
    cleaned_text = re.sub(
        r"[\n\r]+", " ", text
    )  # Replace sequences of newline or carriage return characters with a single space
    return cleaned_text


def expand_contractions(text):
    expanded_text = contractions.fix(text)
    return expanded_text


def clean_compound_words(text):
    # Define the regular expression pattern to match hyphens, slashes, or underscores
    pattern = r"[-/_.]"
    # Use re.sub to replace hyphens, slashes, or underscores with spaces
    cleaned_text = re.sub(pattern, " ", text)
    return cleaned_text


def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    if tag == "J":
        return wordnet.ADJ
    elif tag == "V":
        return wordnet.VERB
    elif tag == "N":
        return wordnet.NOUN
    elif tag == "R":
        return wordnet.ADV
    else:
        # Default to initial word
        return wordnet.NOUN


def lemmatize_word(word):
    lemmatizer = WordNetLemmatizer()
    pos = get_wordnet_pos(word)
    lemma = lemmatizer.lemmatize(word, pos)
    return lemma


def clean_text(text):
    """Function to clean and preprocess text data."""

    # Remove HTML tags
    text = clean_html_tags(
        clean_html_tags(text)
    )  # we do it twice because who knows ... actually it is a real issue

    # Remove newlines \n and \r
    text = clean_newlines(text)

    # Handle/Expand contractions
    text = expand_contractions(text)

    # Separate compound words into individual words
    text = clean_compound_words(text)

    # Convert text to lowercase
    text = text.lower()

    text = replace_programming_language_name(text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english") + ["use", "would", "like"])
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization
    lemmatized_tokens = [lemmatize_word(word) for word in filtered_tokens]

    # Join tokens back into a single string
    clean_text = " ".join(lemmatized_tokens)

    return clean_text
