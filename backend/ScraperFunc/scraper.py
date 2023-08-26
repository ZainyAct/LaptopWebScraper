from bs4 import BeautifulSoup
import requests

def get_laptop_data():
    laptops_data = []

    html_text = requests.get("https://www.canadacomputers.com/promotions/back-to-school-2023")
    soup = BeautifulSoup(html_text.content, 'html.parser')

    laptop_divs = soup.find_all('div', class_='col-12 productImageDesc')

    for laptop_div in laptop_divs:
        # Extract laptop name and link
        laptop_name_link = laptop_div.find('a', class_='text-dark text-truncate_3')
        laptop_name = laptop_name_link.text
        laptop_link = laptop_name_link['href']

        # Extract initial and final price
        initial_price_span = laptop_div.find('span', class_='d-sm-block line-height').find('s')
        initial_price = initial_price_span.get_text(strip=True) if initial_price_span else None

        final_price_span = laptop_div.find('span', class_='text-danger d-block mb-0 pq-hdr-product_price line-height')
        final_price = final_price_span.strong.get_text(strip=True) if final_price_span else None

        # Extract savings
        savings_tooltip = laptop_div.find('div', class_='d-inline-block pt-0_5')
        savings = savings_tooltip.get_text(strip=True).replace("SAVE", "").replace("$", "")
        laptops_data.append({
            'name': laptop_name,
            'link': laptop_link,
            'initial_price': initial_price,
            'final_price': final_price,
            'savings': savings,
        })

    return laptops_data
