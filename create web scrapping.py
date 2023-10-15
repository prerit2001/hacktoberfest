import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract specific elements from the page
    articles = soup.find_all('article')  # Modify this selector based on the site's structure

    # Loop through the extracted elements and print their titles
    for article in articles:
        title = article.find('h2').text  # Modify this selector based on the site's structure
        print(title)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
