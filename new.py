import requests
from bs4 import BeautifulSoup
import csv
# Make a request
page = requests.get(
    "https://www.bbc.com/bengali")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list
all_products = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.css-8tq3w8 ezetrkd0')
for product in products:
    name = product.select('h3 > a')[0].text.strip()
    description = product.select('p.css-193xxgh-Summary e1tfxkuo4')[0].text.strip()
    price = product.select('time.css-lt7vf0-StyledTimestamp e4zesg50')[0].text.strip()
   # reviews = product.select('div.ratings')[0].text.strip()
    #image = product.select('img')[0].get('src')

    all_products.append({
        "name": name,
        "description": description,
        "price": price,
        #"reviews": reviews,
        #"image": image
    })


keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)