import re
import requests

def extract_email(text):
    match = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match[0] if match else None

def extract_phone(text):
    match = re.findall(r"\+?\d[\d -]{8,12}\d", text)
    return match[0] if match else None

def contact_agent(profile):
    url = profile.get("website")
    
    email = None
    phone = None

    if url:
        try:
            res = requests.get(url, timeout=5)
            text = res.text

            email = extract_email(text)
            phone = extract_phone(text)
        except:
            pass

    return {
        "email": email if email else "Not available",
        "phone": phone if phone else "Not available",
        "source": url if url else "Not available"
    }