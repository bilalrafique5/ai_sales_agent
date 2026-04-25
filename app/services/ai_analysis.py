import os
from dotenv import load_dotenv
from groq import GroqClient  # Make sure the Groq SDK is installed

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize client
client = GroqClient(api_key=GROQ_API_KEY)

def analyze_company(company_description: str) -> str:
    """
    Analyze a company using Groq SDK.
    """
    prompt = (
        f"Analyze this company for sales opportunities and provide insights:\n\n"
        f"{company_description}"
    )

    response = client.generate(
        model="groq-sales-1",  # Your Groq model name
        prompt=prompt,
        max_output_tokens=300
    )

    return response.text if hasattr(response, "text") else str(response)