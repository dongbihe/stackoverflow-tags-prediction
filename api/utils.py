import numpy as np
from sentence_transformers import SentenceTransformer

from api.preprocessing import clean_text


def get_bert_embeddings(text):
    model = SentenceTransformer("bert-base-nli-mean-tokens")
    bert_embeddings = model.encode(clean_text(text))
    return bert_embeddings.reshape((1, 768))


def predict_tags(loaded_model, embeddings, top_tags):
    pred_labels = loaded_model.predict(embeddings)
    pred_tags = np.array(top_tags)[pred_labels[0] == 1]
    return pred_tags
