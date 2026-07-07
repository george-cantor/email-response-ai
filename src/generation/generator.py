import os
import re

from dotenv import load_dotenv
import google.generativeai as genai

from src.config import GEMINI_MODEL


class EmailGenerator:

    def __init__(self):

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

        self.model = genai.GenerativeModel(
            GEMINI_MODEL
        )

    def generate(
        self,
        query,
        context
    ):

        prompt = f"""
You are a professional email assistant.

Generate exactly ONE professional reply.

Do not provide multiple options.

Incoming Email:
{query}

Relevant Examples:
{context}

Return only the reply.
"""

        try:

            response = self.model.generate_content(
                prompt
            )

            return response.text.strip()

        except Exception as e:

            print("\nGemini Error:")
            print(e)

            print(
                "\nUsing retrieved reply as fallback..."
            )

            matches = re.findall(
                r"Past Reply:\s*(.*?)(?=\n\s*Past Email:|\Z)",
                context,
                re.DOTALL
            )

            if matches:

                return matches[0].strip()

            return (
                "Thank you for contacting us. "
                "We have received your request and "
                "will get back to you shortly."
            )