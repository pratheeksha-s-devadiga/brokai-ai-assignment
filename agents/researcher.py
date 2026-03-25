from utils.search import search_company

def clean_summary(text):
    if not text:
        return "No info found"

    text = text.replace("â€¦", "").replace("Â", "")
    return text[:200]


def research_agent(company, location):
    query = f"{company} {location} solar energy company India"

    results = search_company(query)

    summary = "No info found"
    website = ""

    for r in results:
        snippet = r["snippet"].lower()

        if any(word in snippet for word in [
            "solar", "energy", "power", "electrical", "services"
        ]):
            summary = clean_summary(r["snippet"])
            website = r["link"]
            break

    if results:
        if website == "":
            website = results[0]["link"]

        if summary == "No info found":
            summary = clean_summary(results[0]["snippet"])

    return {
        "company": company,
        "location": location,
        "summary": summary,
        "website": website
    }