import requests

def fetch_randomProduct():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    res_data = response.json()

    if res_data["success"] and "data" in res_data:
        product_details = res_data["data"]
        id = product_details["id"]
        title = product_details["title"]
        description = product_details["description"]
        price = product_details["price"]
        discount = product_details["discountPercentage"]
        rating = product_details["rating"]
        stocks = product_details["stock"]
        brand = product_details["brand"]
        category = product_details["category"]
        image = product_details["thumbnail"]

        return (product_details, id, title, description, price, discount, rating, stocks, brand, category, image)
    else:
        raise Exception("Failed to fetch Product data")
    

def main():
    try:
        product_details, id, title, description, price, discount, rating, stocks, brand, category, image = fetch_randomProduct()
        # print(product_details)
        # print(type(product_details))
        print(f"Id: {id} \nProduct name: {title} \nProduct detail: {description} \nPrice: ${price} \nDiscount: {discount}% \nRatings: {rating} \nStock Unit: {stocks} \nBrand: {brand} \nProduct Category: {category} \nProduct View: {image}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()