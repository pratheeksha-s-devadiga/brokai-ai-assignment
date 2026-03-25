def outreach_agent(profile, contact):
    company = profile["company"]
    summary = profile["summary"]

    if summary == "No info found":
        summary = "you are operating in the solar/energy business"

    message = f"""
Hi, I came across {company} and noticed that {summary[:80]}.

We help businesses like yours automate customer calls, lead handling, and support using AI voice agents.

Would you be open to a quick demo?

Thanks!
"""

    return message.strip()