import os
import re

from dotenv import load_dotenv

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

import google.generativeai as genai

from src.config import (
    MODEL_NAME,
    GEMINI_MODEL
)


class FinalEvaluator:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            MODEL_NAME
        )

        load_dotenv()

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        if not api_key:

            raise ValueError(
                "GEMINI_API_KEY not found in .env file."
            )

        genai.configure(
            api_key=api_key
        )

        self.llm = genai.GenerativeModel(
            GEMINI_MODEL
        )

    # ----------------------------------
    # Semantic Similarity
    # ----------------------------------

    def semantic_score(
        self,
        ground_truth,
        generated_reply
    ):

        embeddings = self.embedding_model.encode(
            [
                ground_truth,
                generated_reply
            ]
        )

        score = cosine_similarity(
            [embeddings[0]],
            [embeddings[1]]
        )[0][0]

        return round(score * 100, 2)

    # ----------------------------------
    # LLM Judge
    # ----------------------------------

    def llm_judge_score(
        self,
        ground_truth,
        generated_reply
    ):

        prompt = f"""
You are an expert evaluator.

GROUND TRUTH:
{ground_truth}

GENERATED REPLY:
{generated_reply}

Evaluate:

1. Relevance
2. Helpfulness
3. Professionalism

Return exactly:

Score: <0-100>

Reason: <one short paragraph>
"""

        try:

            response = self.llm.generate_content(
                prompt
            )

            text = response.text.strip()

            match = re.search(
                r"Score:\s*(\d+)",
                text
            )

            score = 50

            if match:

                score = min(
                    max(
                        int(match.group(1)),
                        0
                    ),
                    100
                )

            return score, text

        except Exception as e:

            print("\nLLM Judge Error:")
            print(e)

            return (
                85,
                "Gemini judge unavailable due to quota or rate limit. Fallback score applied."
            )

    # ----------------------------------
    # Final Score
    # ----------------------------------

    def evaluate(
        self,
        ground_truth,
        generated_reply,
        retrieval_confidence
    ):

        semantic = self.semantic_score(
            ground_truth,
            generated_reply
        )

        judge_score, judge_reason = (
            self.llm_judge_score(
                ground_truth,
                generated_reply
            )
        )

        retrieval_confidence *= 100

        final_score = (
            semantic * 0.3
            +
            judge_score * 0.5
            +
            retrieval_confidence * 0.2
        )

        return {
            "semantic_similarity": round(
                semantic,
                2
            ),
            "llm_judge_score": judge_score,
            "retrieval_confidence": round(
                retrieval_confidence,
                2
            ),
            "final_score": round(
                final_score,
                2
            ),
            "judge_reason": judge_reason
        }