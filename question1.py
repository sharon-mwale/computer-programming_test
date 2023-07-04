import requests
from bs4 import BeautifulSoup

html = '''
<div class="books-list">
    <div class="book">
        <h2 class="title">Book 1</h2>
        <p class="author">Author 1</p>
        <span class="price">$10</span>
    </div>
    <div class="book">
        <h2 class="title">Book 2</h2>
        <p class="author">Author 2</p>
        <span class="price">$15</span>
    </div>
</div>
'''


# Send a GET request to the web page
url = 'https://www.example.com/books'
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the book listings on the page
book_listings = soup.find_all('div', class_='book-listing')

# Create an empty list to store the book data
books = []

# Extract the title, author, and price of each book
for listing in book_listings:
    title = listing.find('h2').text
    author = listing.find('p', class_='author').text
    price = listing.find('span', class_='price').text

    # Create a dictionary for the book and add it to the list
    book = {
        'title': title,
        'author': author,
        'price': price
    }
    books.append(book)

# Print the list of books
for book in books:
    print(book)
