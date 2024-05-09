import os
import numpy as np
import pandas as pd
from flask import Flask, jsonify
from joblib import load

from api.preprocessing import clean_text

app = Flask(__name__)


@app.route("/api/text=<text>")
def my_api(text):
    """
    API route to process the input text and return the tags.

    Parameters:
        text (str): The input text from the user.

    Returns:
        JSON: A JSON object containing the input text and the predicted tags.
    """

    # embeddings = get_bert_embeddings(text)
    # tags_prediction = predict_tags(loaded_model, embeddings, TOP_TAGS)
    tags_prediction = ["python", "array"]
    # tags_prediction = []
    if len(tags_prediction) == 0:
        tags_prediction = "No tags suggested"
    # data = {"text": [text], "tags": [", ".join(tags_prediction)]}
    data = {"text": [text], "tags": [tags_prediction]}

    return jsonify(data)
