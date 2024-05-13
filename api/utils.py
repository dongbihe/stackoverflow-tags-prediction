from sentence_transformers import SentenceTransformer

from api.preprocessing import clean_text


from api.static_data import MODEL, TOP_TAGS


def get_bert_embeddings(text):
    pretrained_model = SentenceTransformer("bert-base-nli-mean-tokens")
    cleaned_text = clean_text(text)
    bert_embeddings = pretrained_model.encode(cleaned_text)
    return bert_embeddings.reshape((1, 768))


def predict_tags(embeddings, loaded_model=MODEL, top_tags=TOP_TAGS):
    pred_labels = loaded_model.predict(embeddings)
    pred_tags = top_tags[pred_labels[0] == 1]
    return list(pred_tags)
