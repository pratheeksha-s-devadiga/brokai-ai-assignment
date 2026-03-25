from duckduckgo_search import DDGS

def search_company(query):
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=8):

            link = r["href"]

            if any(x in link for x in [
                "wikipedia",
                "zhihu",
                "baidu",
                "stackoverflow",
                "quora"
            ]):
                continue

            results.append({
                "title": r["title"],
                "link": link,
                "snippet": r["body"]
            })

    return results