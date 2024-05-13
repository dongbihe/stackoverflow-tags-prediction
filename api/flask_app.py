from flask import Flask, jsonify

from api.utils import get_bert_embeddings, predict_tags


app = Flask(__name__)


@app.route("/")
def hello():
    """
    Default route to display "Hello World!" message just to test you are good with flask :).
    """
    return "Hello World!"


@app.route("/api/text=<text>")
def my_api(text):
    """
    API route to process the input text and return the tags.

    Parameters:
        text (str): The input text from the user.

    Returns:
        JSON: A JSON object containing the input text and the predicted tags.
    """

    embeddings = get_bert_embeddings(text)
    tags_prediction = predict_tags(embeddings)

    if len(tags_prediction) == 0:
        tags_prediction = "No tags suggested"
    # data = {"text": [text], "tags": [", ".join(tags_prediction)]}
    data = {"text": [text], "tags": [tags_prediction]}

    return jsonify(data)
