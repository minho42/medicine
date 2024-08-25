import json
import requests

def wiki_summary(title: str) -> str:
    assert title
    wiki_api_base = (
        "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&redirects&format=json&titles="
    )
    url = f"{wiki_api_base}{title}"
    s = requests.session()
    r = s.get(url)
    r_dict = json.loads(r.text)
    page_num = next(iter(r_dict["query"]["pages"]))
    try:
        summary = r_dict["query"]["pages"][page_num]["extract"]
        summary = summary.strip()
    except KeyError:
        summary = ""
    return summary
