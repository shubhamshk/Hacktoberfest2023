import requests
from bs4 import BeautifulSoup

# Target website
url = "https://quotes.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quote elements
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    print("Quotes from the website:\n")
    for quote, author in zip(quotes, authors):
        print(f"{quote.text} — {author.text}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
