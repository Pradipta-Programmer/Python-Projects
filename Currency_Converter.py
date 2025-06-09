# @@ -1,3 +1,5 @@
# Copyright (c) 2025 Pradipta Singha
# This code is licensed under the MIT License.
import requests
from datetime import datetime

# Prompts user for input and returns required data for currency conversion
def asker():
    api = input("\nEnter your own generated API key:  ").strip()
    country(api)  # Display the list of supported currency codes
    base = input("\nEnter the base currency (e.g., USD): ").strip().upper()
    target = input("Enter the target currency (e.g., INR): ").strip().upper()
    amount = input("Enter the number as amount to be converted: ").strip()
    return api, base, target, amount

# Fetches and displays available currency codes from the API
def country(api):
    print("Here is a list of country codes")
    response = requests.get(f"https://api.exchangerate.host/list?access_key={api}")
    response = response.json()

    if not response.get("success", False):
        print("⚠️ Could not fetch currency list. Continuing without it.\n")
        return

    symbols = list(response["currencies"].items())

    for i in range(0, len(symbols), 5):
        for code, name in symbols[i:i+5]:
            print(f"{code}: {name}", end="  ||  ")
        print()

while True:
    while True:
        api, base, target, amount = asker()

        url = f"https://api.exchangerate.host/convert?from={base}&to={target}&amount={amount}&access_key={api}"
        response = requests.get(url)
        data = response.json()

        if data["success"] == True:
            # Successful conversion result with timestamp
            print(f"\n{amount} {base} is equal to {data['result']} {target} "
                  f"according to the current time "
                  f"{datetime.fromtimestamp(data['info']['timestamp']).strftime('%I:%M %p')} IST \n")
            break
        else:
            # Different error code interpretation
            if data["error"]["code"] == 101:
                print("\n ⚠️ Wrong/Invalid API key ⚠️")
            elif data["error"]["code"] == 401:
                print("\n ⚠️ Invalid Base Currency ⚠️")
            elif data["error"]["code"] == 402:
                print("\n ⚠️ Invalid Target Currency ⚠️")
            elif data["error"]["code"] == 403:
                print("\n ⚠️ Invalid Amount ⚠️")
            else:
                print("Something Went Wrong\nTry Again\n")

    while True:
        option = input("\nWant to use it again? Y/N \n>>> ").lower()
        if option in ["yes", "y"]:
            break
        elif option in ["no", "n"]:
            print("\nThank you for using my Currency Converter 😊")
            exit()
        else:
            print("\nInvalid Input\nTry Again")
