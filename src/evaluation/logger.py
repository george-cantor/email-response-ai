import os
import pandas as pd

from src.config import RESULTS_PATH


def save_result(
    email,
    generated_reply,
    semantic,
    judge,
    retrieval,
    final_score
):

    row = {
        "email": email,
        "generated_reply": generated_reply,
        "semantic_similarity": semantic,
        "llm_judge_score": judge,
        "retrieval_confidence": retrieval,
        "final_score": final_score
    }

    output_file = RESULTS_PATH

    os.makedirs(
        os.path.dirname(output_file),
        exist_ok=True
    )

    if (
        os.path.exists(output_file)
        and
        os.path.getsize(output_file) > 0
    ):

        df = pd.read_csv(
            output_file
        )

        df = pd.concat(
            [
                df,
                pd.DataFrame([row])
            ],
            ignore_index=True
        )

    else:

        df = pd.DataFrame(
            [row]
        )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"\nResults saved to {output_file}"
    )