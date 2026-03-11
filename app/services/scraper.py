import requests
from bs4 import BeautifulSoup


def scrape_company_data(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "Unknown"

    description = ""

    meta = soup.find("meta", attrs={"name": "description"})

    if meta:
        description = meta.get("content")

    return {
        "company_name": title,
        "description": description,
        "website": url
    }