import pandas as pd
from agents.researcher import research_agent
from agents.contact_finder import contact_agent
from agents.outreach_writer import outreach_agent

def process_excel(file):

    df = pd.read_excel(file, header=None)

    df = df.iloc[1:]

    results = []

    for _, row in df.head(10).iterrows():

        location = str(row.iloc[2]).strip()
        company = str(row.iloc[3]).strip()
        email_excel = str(row.iloc[4])
        phone_excel = str(row.iloc[5])

        if company.lower() == "nan" or company == "":
            company = "Unknown Company"

        email_excel = email_excel.replace("Email :", "").replace("[at]", "@").replace("[dot]", ".").strip()

        phone_excel = phone_excel.strip()

        try:
           
            if "E+" in phone_excel or "e+" in phone_excel:
                phone_excel = str(int(float(phone_excel)))
        except:
            pass

        phone_excel = phone_excel.replace(" ", "")

        
        if phone_excel.lower() == "nan" or phone_excel == "":
            phone_excel = "Not available"

        profile = research_agent(company, location)
        contact = contact_agent(profile)

        if email_excel and "@" in email_excel:
            contact["email"] = email_excel

        if phone_excel != "Not available":
            contact["phone"] = phone_excel

        message = outreach_agent(profile, contact)

        results.append({
            "Company": company,
            "Summary": profile["summary"] if profile["summary"] != "No info found" 
           else f"{company} operates in the {location} region in the solar/energy domain.",
            "Website": profile["website"],
            "Email": contact["email"],
            "Phone": contact["phone"],
            "Source": contact["source"],
            "Message": message
        })

    return pd.DataFrame(results)