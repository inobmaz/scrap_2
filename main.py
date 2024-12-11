from urllib.request import urlopen

def fetch_title(url):
    try:
        # Use the passed `url` parameter
        page = urlopen(url)
        html = page.read().decode("utf-8")
        start_index = html.find("<title>") + len("<title>")
        end_index = html.find("</title>")
        return html[start_index:end_index]
    except Exception as e:
        return f"Error: {e}"

# Pass the URL as an argument
url = "http://olympus.realpython.org/profiles/poseidon"
print(fetch_title(url))


