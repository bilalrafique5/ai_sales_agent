from fastapi import APIRouter
from app.models.lead_model import Lead
from app.database import leads_collection
from app.services.scraper import scrape_company_data
from app.services.ai_analysis import analyze_company
from app.services.outreach_generator import generate_outreach

router = APIRouter()


@router.post("/research-lead")
def research_lead(lead: Lead):

    company_data = scrape_company_data(lead.website)

    analysis = analyze_company(company_data["description"])

    outreach = generate_outreach(
        lead.decision_maker,
        lead.company_name,
        analysis
    )

    data = {
        "lead": lead.dict(),
        "company_data": company_data,
        "analysis": analysis,
        "outreach": outreach
    }

    leads_collection.insert_one(data)

    return data