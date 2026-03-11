from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_outreach(name, company, analysis):

    prompt = f"""
    Write a short personalized cold outreach email.

    Decision Maker: {name}
    Company: {company}

    Analysis:
    {analysis}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text