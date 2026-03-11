from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_company(company_description):

    prompt = f"""
    Analyze this company and identify:

    1. Possible business pain points
    2. Sales opportunities
    3. Potential services they might need

    Company Description:
    {company_description}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text