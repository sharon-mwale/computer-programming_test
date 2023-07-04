from bs4 import BeautifulSoup

def scrape_books_data(html):
    soup = BeautifulSoup(html, "html.parser")
    books_list = soup.find("div", class_="books-list")
    
    books = []
    
    for book_div in books_list.find_all("div", class_="book"):
        title = book_div.find("h2", class_="title").text
        author = book_div.find("p", class_="author").text
        price = book_div.find("span", class_="price").text
        
        book = {
            "title": title,
            "author": author,
            "price": price
        }
        
        books.append(book)
    
    return books

def get_average_price(soup):
    books = soup.find_all("div", class_="book")
    total_price = 0
    num_books = len(books)
    
    for book in books:
        price_text = book.find("span", class_="price").text
        price = float(price_text.replace("K", ""))
        total_price += price
    
    if num_books > 0:
        average_price = total_price / num_books
        return average_price
    else:
        return 0.0


# HTML structure of the web page
html = """
<div class="books-list">
    <div class="book">
        <h2 class="title">Game Of Thones</h2>
        <p class="author">Petter Parker</p>
        <span class="price">K150</span>
    </div>
    <div class="book">
        <h2 class="title">How To Lose A Guy In 10 Days</h2>
        <p class="author">Cassy Jones</p>
        <span class="price">K170</span>
    </div>
</div>
"""

# Scrape the books data from the HTML
books_data = scrape_books_data(html)

# Print the list of books
for book in books_data:
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("Price:", book["price"])
    print()

# Create a Beautiful Soup object from the HTML
soup = BeautifulSoup(html, "html.parser")

# Calculate and print the average price
average_price = get_average_price(soup)
print("Average price:", average_price)
