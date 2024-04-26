import os
import numpy as np
import pandas as pd
from flask import Flask, jsonify
from joblib import load

from api.preprocessing import clean_text
#from api.utils import get_bert_embeddings, predict_tags

# mlflow.set_tracking_uri("http://127.0.0.1:7000")
# logged_model = "runs:/2598301c656e4a308b27e241eca31fc0/multi_output_classifier_XGBoost"
# loaded_model = mlflow.pyfunc.load_model(logged_model)


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

    #embeddings = get_bert_embeddings(text)
    # tags_prediction = predict_tags(loaded_model, embeddings, TOP_TAGS)
    tags_prediction = ["python", "array"]
    # tags_prediction = []
    if len(tags_prediction) == 0:
        tags_prediction = "No tags suggested"
    # data = {"text": [text], "tags": [", ".join(tags_prediction)]}
    data = {"text": [text], "tags": [tags_prediction]}

    return jsonify(data)
