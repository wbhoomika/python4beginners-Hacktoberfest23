import requests
from bs4 import BeautifulSoup

def fetch_books_data():
    #replace https://www.examplebookswebsite.com with some website of your choice
    url = "https://www.examplebookswebsite.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        book_list = soup.find_all('div', class_='book-item')

        for book in book_list:
            title = book.find('h2', class_='book-title').text
            author = book.find('p', class_='book-author').text
            price = book.find('span', class_='book-price').text

            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Price: {price}")
            print()

    else:
        print("Failed to fetch data. Status code:", response.status_code)

if __name__ == "__main__":
    fetch_books_data()