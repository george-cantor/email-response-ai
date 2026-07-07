import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from src.config import (
    MODEL_NAME,
    DATA_PATH,
    TOP_K
)


class EmailRetriever:

    def __init__(self):

        self.df = pd.read_csv(
            DATA_PATH
        )

        if self.df.empty:

            raise ValueError(
                "Dataset is empty."
            )

        self.model = SentenceTransformer(
            MODEL_NAME
        )

        self.email_embeddings = self.model.encode(
            self.df["email"].tolist()
        )

    def retrieve(
        self,
        query,
        top_k=TOP_K
    ):

        query_embedding = self.model.encode(
            [query]
        )

        similarities = cosine_similarity(
            query_embedding,
            self.email_embeddings
        )[0]

        top_indices = similarities.argsort()[
            -top_k:
        ][::-1]

        return (
            self.df,
            top_indices,
            similarities
        )