from bs4 import BeautifulSoup

def get_average_price(soup):
    prices = soup.find_all("span", class_="price")
    total_price = 0
    num_books = len(prices)
    
    for price in prices:
        price_text = price.get_text().strip().replace("$", "")
        total_price += float(price_text)
    
    if num_books > 0:
        average_price = total_price / num_books
        return average_price
    else:
        return 0.0

# Test the function with the provided HTML structure
html = """
<html>
<body>
  <div class="book">
    <h2>Title 1</h2>
    <span class="price">$10.99</span>
  </div>
  <div class="book">
    <h2>Title 2</h2>
    <span class="price">$15.99</span>
  </div>
  <div class="book">
    <h2>Title 3</h2>
    <span class="price">$12.99</span>
  </div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
average_price = get_average_price(soup)
print("Average price:", average_price)
