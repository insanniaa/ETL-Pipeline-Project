import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import numpy as np

def extract_product_data():
    base_url = "https://fashion-studio.dicoding.dev"
    all_products = []
    try:
        for page in range(1, 51):
            if page == 1:
                url = base_url
            else:
                url = f"{base_url}/page{page}"
            
            print(f"Extracting from: {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            products = soup.find_all("div", class_="collection-card")

            print(f"Page {page}: Found {len(products)} products")

            for product in products:
                title = product.find("h3", class_="product-title").text.strip()
                
                #untuk extract harga
                price = product.find("span", class_="price")
                price = price.text.strip() if price else "N/A"

                #untuk extract rating
                rating_text = product.find("p", string=lambda text: "Rating:" in text)
                if rating_text and "Invalid Rating" not in rating_text.text:
                    rating = rating_text.text.replace("Rating:", "").replace("/ 5", "").strip()
                else:
                    rating = np.nan
                
                #untuk extract colors
                colors_text = product.find("p", string=lambda text: "Colors" in text)
                colors = int(colors_text.text.split()[0]) if colors_text else 0
                
                #untuk extract size
                size_text = product.find("p", string=lambda text: "Size:" in text)
                size = size_text.text.replace("Size:", "").strip() if size_text else "N/A"

                #untuk extract gender
                gender_text = product.find("p", string=lambda text: "Gender:" in text)
                gender = gender_text.text.replace("Gender:", "").strip() if gender_text else "N/A"

                timestamp = datetime.datetime.now().isoformat()
                
                all_products.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Colors": colors,
                    "Size": size,
                    "Gender": gender,
                    "Timestamp": timestamp
                })
    except Exception as e:
        print(f"Error in extract_product_data: {e}")
    
    print(f"\nTotal products found: {len(all_products)}")
    return pd.DataFrame(all_products)
