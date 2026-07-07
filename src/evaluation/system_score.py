import os
import pandas as pd

from src.config import RESULTS_PATH


def calculate_system_score():

    if not os.path.exists(
        RESULTS_PATH
    ):

        print(
            "\nNo results file found."
        )

        return

    if os.path.getsize(
        RESULTS_PATH
    ) == 0:

        print(
            "\nResults file is empty."
        )

        return

    df = pd.read_csv(
        RESULTS_PATH
    )

    if df.empty:

        print(
            "\nNo evaluation records found."
        )

        return

    avg_semantic = df[
        "semantic_similarity"
    ].mean()

    avg_judge = df[
        "llm_judge_score"
    ].mean()

    avg_retrieval = df[
        "retrieval_confidence"
    ].mean()

    avg_final = df[
        "final_score"
    ].mean()

    best_email = df.loc[
        df["final_score"].idxmax()
    ]

    print("\n" + "=" * 50)
    print("SYSTEM PERFORMANCE REPORT")
    print("=" * 50)

    print(
        f"Average Semantic Similarity : "
        f"{avg_semantic:.2f}"
    )

    print(
        f"Average LLM Judge Score     : "
        f"{avg_judge:.2f}"
    )

    print(
        f"Average Retrieval Confidence: "
        f"{avg_retrieval:.2f}"
    )

    print(
        f"Average Final Score         : "
        f"{avg_final:.2f}"
    )

    print("\nBest Performing Email")

    print(
        best_email["email"]
    )

    print(
        f"Score: {best_email['final_score']:.2f}"
    )

    print("=" * 50)