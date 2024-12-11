# Fetch Title Utility

## Overview
This Python script is designed to fetch and extract the `<title>` tag content from a specified webpage. It is a simple demonstration of basic web scraping using Python’s built-in libraries.

---

## Features
- Fetches HTML content from a given URL.
- Extracts the `<title>` tag content from the HTML.
- Includes error handling for network and parsing issues.

---

## Prerequisites
Ensure the following are installed on your system:

- **Python 3.x**
- Internet connection to access the target webpage

---

## Installation
1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script.

---

## Usage
1. Open the script file (`fetch_title.py`) in any code editor.
2. Specify the target URL:
   ```python
   url = "http://example.com"
   ```
3. Run the script:
   ```bash
   python fetch_title.py
   ```
4. The extracted title will be printed in the terminal.

### Example Output
If the webpage’s title is `Poseidon - Profile Page`, the script will output:
```bash
Poseidon - Profile Page
```

---

## Code Walkthrough
### Core Function
```python
from urllib.request import urlopen

def fetch_title(url):
    try:
        page = urlopen(url)
        html = page.read().decode("utf-8")
        start_index = html.find("<title>") + len("<title>")
        end_index = html.find("</title>")
        return html[start_index:end_index]
    except Exception as e:
        return f"Error: {e}"
```
This function:
1. Opens a connection to the specified URL using `urlopen`.
2. Decodes the HTML content to UTF-8.
3. Searches for the `<title>` tag and extracts its content using string manipulation.
4. Handles exceptions and returns an error message if something goes wrong.

### Example Call
```python
url = "http://olympus.realpython.org/profiles/poseidon"
print(fetch_title(url))
```
This example demonstrates how to use the `fetch_title` function to fetch the title from a predefined URL.

---

## Potential Enhancements
1. **Use Libraries for Parsing**:
   Switch to a robust library like `BeautifulSoup` for better HTML parsing and to handle edge cases.
2. **Dynamic Input**:
   Allow users to input the URL dynamically via the command line or a configuration file.
3. **Error Logging**:
   Add logging for better debugging and tracking of issues.
4. **Testing**:
   Implement unit tests to verify functionality with different types of HTML content.

---

## License
This project is open-source and available under the MIT License.

