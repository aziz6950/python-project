from requests import get
from pprint import PrettyPrinter

API_KEY = "b4dc0323a4797ec9b7b01ccf"

printer = PrettyPrinter()

def get_rates(base_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
    response = get(url)
    
    if response.status_code != 200:
        print("Error connecting to API")
        return None
    
    data = response.json()
    
    if data["result"] != "success":
        print("Invalid API request")
        return None
    
    return data["conversion_rates"]


def convert_currency():
    base = input("Enter base currency (e.g. USD): ").upper()
    target = input("Enter target currency (e.g. BDT): ").upper()
    amount = float(input("Enter amount: "))
    
    rates = get_rates(base)
    
    if rates is None:
        return
    
    if target not in rates:
        print("Invalid target currency!")
        return
    
    converted = amount * rates[target]
    
    print(f"\n{amount} {base} = {converted:.2f} {target}")


# Run program
convert_currency()





























































