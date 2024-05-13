import joblib
import numpy as np

MODEL = joblib.load("api/data/xgboost_bert_200_tags.sav")
TOP_TAGS = np.load("api/data/top_200_tags.npy")
