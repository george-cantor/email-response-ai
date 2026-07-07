from src.evaluation.system_score import (
    calculate_system_score
)

from src.retrieval.retriever import (
    EmailRetriever
)

from src.generation.generator import (
    EmailGenerator
)

from src.evaluation.final_evaluator import (
    FinalEvaluator
)

from src.evaluation.logger import (
    save_result
)


def main():

    try:

        retriever = EmailRetriever()

        generator = EmailGenerator()

        evaluator = FinalEvaluator()

        query = input(
            "\nEnter Email: "
        ).strip()

        if not query:

            print(
                "\nPlease enter a valid email."
            )

            return

        df, top_indices, similarities = (
            retriever.retrieve(query)
        )

        if len(top_indices) == 0:

            print(
                "\nNo similar emails found."
            )

            return

        # ----------------------------------
        # Build Context
        # ----------------------------------

        context = ""

        for idx in top_indices:

            context += f"""
Past Email:
{df.iloc[idx]['email']}

Past Reply:
{df.iloc[idx]['reply']}
"""

        # ----------------------------------
        # Best Retrieved Reply
        # ----------------------------------

        best_reply = df.iloc[
            top_indices[0]
        ]["reply"]

        # ----------------------------------
        # Generate Reply
        # ----------------------------------

        generated_reply = generator.generate(
            query,
            context
        )

        print("\n" + "=" * 60)

        print("\nGENERATED REPLY\n")

        print(generated_reply)

        # ----------------------------------
        # Evaluation
        # ----------------------------------

        results = evaluator.evaluate(
            ground_truth=best_reply,
            generated_reply=generated_reply,
            retrieval_confidence=
            similarities[top_indices[0]]
        )

        # ----------------------------------
        # Save Results
        # ----------------------------------

        save_result(
            email=query,
            generated_reply=generated_reply,
            semantic=results[
                "semantic_similarity"
            ],
            judge=results[
                "llm_judge_score"
            ],
            retrieval=results[
                "retrieval_confidence"
            ],
            final_score=results[
                "final_score"
            ]
        )

        # ----------------------------------
        # Display Results
        # ----------------------------------

        print("\n" + "=" * 60)

        print("\nEVALUATION\n")

        for key, value in results.items():

            print(
                f"{key}: {value}"
            )

        # ----------------------------------
        # Overall System Report
        # ----------------------------------

        calculate_system_score()

    except Exception as e:

        print(
            f"\nApplication Error: {e}"
        )


if __name__ == "__main__":

    main()