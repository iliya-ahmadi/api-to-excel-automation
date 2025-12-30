from api_client import fetch_products
from excel_exporter import export_to_excel
import os 

os.makedirs('output',exist_ok=True)
API_URL = "https://fakestoreapi.com/products"
OUTPUT_FILE = "output/prodects_report.xlsx"

def main():
    products = fetch_products(API_URL)

    if not products:
        print('no products fetched. Exiting')
        return
    
    items = []
    for product in products:
        items.append({
            "product_name": product.get("title",''),
            "price": product("price",0),
            "category": product("category",''),
            "rating_count": product.get("rating",{}).get("count",0)
        })

    export_to_excel(items, OUTPUT_FILE)

if __name__ == "__main__":
    main()


    