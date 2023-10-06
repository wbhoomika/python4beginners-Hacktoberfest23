import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape quotes and authors
def scrape_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = []
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            quotes.append((text, author, tags))
        return quotes
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

# Function to save quotes to a CSV file
def save_quotes_to_csv(quotes, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Quote', 'Author', 'Tags'])
        csv_writer.writerows(quotes)

if __name__ == '__main__':
    url = 'http://quotes.toscrape.com'
    quotes = scrape_quotes(url)
    if quotes:
        save_quotes_to_csv(quotes, 'quotes.csv')
        print(f'Scraped {len(quotes)} quotes and saved them to "quotes.csv".')
