# API Handling in Python
import requests

def fetch_randomUserApi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    res_data = response.json()

    if res_data["success"] and "data" in res_data:
        user_data = res_data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        age = user_data["dob"]["age"]
        name_title = user_data["name"]["title"]
        first_name = user_data["name"]["first"]
        last_name = user_data["name"]["last"]
        fullname = f"{name_title} {first_name} {last_name}"
        return (user_data, fullname, age, username, country)
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        user_data, fullname, age, username, country = fetch_randomUserApi()
        # print(user_data)
        print(f"Fullname: {fullname} \nAge: {age} \nUsername: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
