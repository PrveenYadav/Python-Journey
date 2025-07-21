import requests

def fetch_randomQuote():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    res_data = response.json()

    if res_data["success"] and "data" in res_data:
        quote_details = res_data["data"]
        author = quote_details["author"]
        quote = quote_details["content"]
        tag = quote_details["tags"]
        # tag2 = quote_details["tags"][1]
        # tag = f"{tag1} {tag2}"

        return quote_details, author, quote, tag
    else:
        raise Exception("Failed to fetch Quote Details")


def main():
    try:
        quote_details, author, quote, tag = fetch_randomQuote()
        # print(quote_details)
        print(f"Author: {author} \nQuote: {quote} \nTag: {tag[0]}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()