import os
from dotenv import load_dotenv
from groq import GroqClient  # Make sure the Groq SDK is installed

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize client
client = GroqClient(api_key=GROQ_API_KEY)

def generate_outreach(decision_maker: str, company_name: str, analysis: str) -> str:
    """
    Generate a personalized outreach message using Groq SDK.
    """
    prompt = (
        f"Create a personalized outreach email to {decision_maker} at {company_name}.\n\n"
        f"Company insights:\n{analysis}\n\n"
        "Make it concise, professional, and persuasive."
    )

    response = client.generate(
        model="groq-sales-1",  # Your Groq model name
        prompt=prompt,
        max_output_tokens=250
    )

    return response.text if hasattr(response, "text") else str(response)