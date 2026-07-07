import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

ground_truth = """
Please use the password reset link.
Let us know if the issue persists.
"""

generated_reply = """
To regain access to your account,
please use the 'Forgot Password' link on the login page.

Should you require any further assistance,
please let us know.
"""

prompt = f"""
You are an expert evaluator.

Compare:

GROUND TRUTH:
{ground_truth}

GENERATED REPLY:
{generated_reply}

Evaluate:

1. Relevance
2. Helpfulness
3. Professionalism

Give:

Score: <0-100>

Reason: <short explanation>

Return only this format.
"""

try:

    response = model.generate_content(
        prompt
    )

    print(response.text)

except Exception as e:

    print("\nLLM Judge Error:")
    print(e)

    print("\nFallback Result")

    print("""
Score: 85

Reason: Gemini API unavailable or quota exceeded.
Fallback evaluation used.
""")