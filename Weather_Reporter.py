# @@ -1,3 +1,5 @@
# Copyright (c) 2025 Pradipta Singha
# This code is licensed under the MIT License.

import requests
from datetime import datetime

print("Welcome to Weather Reporter 😊")
# Function to get user details and API key
def asker():
    api = input("\nEnter your own generated API key: ").strip()
    user = input("Enter your name: ").strip()
    city = input("Enter the city: ").strip()
    return user, city, api

# Function to generate and write the weather report to a file
def report():
    try:
        # Try creating a new file (fails if it already exists)
        with open(f"Weather_Report_Of_{city}.txt", "x+", encoding="utf-8") as report:
            # Writing formatted data to the file
            report.write(f"City is {city} \n")
            report.write(f"Country is {data['sys']['country']} \n")
            report.write(f"Sunrise & Sunset time is {datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p')} and {datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p')} \n")
            report.write(f"Latitude & Longitude is {data['coord']['lat']} & {data['coord']['lon']} respectively \n")
            report.write(f"Weather is {data['weather'][0]['main']} \n")
            report.write(f"Temperature feels like {data['main']['feels_like']}°C with max temperature {data['main']['temp_max']}°C and min temperature {data['main']['temp_min']}°C \n")
            report.write(f"Pressure is {data['main']['pressure']} hPa and Humidity is {data['main']['humidity']}% \n")
            report.write(f"Visibility is {data['visibility']} m \n")
            report.write(f"Wind Speed is {data['wind']['speed']} m/s \n")

    except FileExistsError:
        # If the file already exists, this will ask user if they want to overwrite it
        while True:
            answer = input("\nA file already exists. Want to replace it with this one? Y/N \n>>> ").lower()
            if answer in ["yes", "y"]:
                # Overwrite existing file
                with open(f"Weather_Report_Of_{city}.txt", "w", encoding="utf-8") as report:
                    report.write(f"City is {city} \n")
                    report.write(f"Country is {data['sys']['country']} \n")
                    report.write(f"Sunrise & Sunset time is {datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p')} and {datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p')} \n")
                    report.write(f"Latitude & Longitude is {data['coord']['lat']} & {data['coord']['lon']} respectively \n")
                    report.write(f"Weather is {data['weather'][0]['main']} \n")
                    report.write(f"Temperature feels like {data['main']['feels_like']}°C with max temperature {data['main']['temp_max']}°C and min temperature {data['main']['temp_min']}°C \n")
                    report.write(f"Pressure is {data['main']['pressure']} hPa and Humidity is {data['main']['humidity']}% \n")
                    report.write(f"Visibility is {data['visibility']} m \n")
                    report.write(f"Wind Speed is {data['wind']['speed']} m/s \n")
                break
            elif answer in ["no", "n"]:
                return
            else:
                print("Invalid Input\nTry Again")

# Main program loop
while True:
    while True:
        user, city, api = asker()

        # Construct the API URL
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

        # Make a request to the API
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # If the response is valid, print weather details
            print("City is", city)
            print(f"Country is {data['sys']['country']}")
            print(f"Sunrise & Sunset time is {datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p')} and {datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p')}")
            print(f"Latitude & Longitude is {data['coord']['lat']} & {data['coord']['lon']} respectively")
            print(f"Weather is {data['weather'][0]['main']}")
            print(f"Temperature feels like {data['main']['feels_like']}°C with max temperature {data['main']['temp_max']}°C and min temperature {data['main']['temp_min']}°C")
            print(f"Pressure is {data['main']['pressure']} hPa and Humidity is {data['main']['humidity']}%")
            print(f"Visibility is {data['visibility']} m")
            print(f"Wind Speed is {data['wind']['speed']} m/s")

            # this part is asking if the user wants to save the report
            while True:
                answer = input("\nDo you want to have the report in a file? Y/N \n>>> ").lower()
                if answer in ["yes", "y"]:
                    report()
                    break
                elif answer in ["no", "n"]:
                    break
                else:
                    print("Invalid Input\nTry Again")
            break
        else:
            # Invalid API key or city name
            print("Invalid City or API key\nTry again please")

    # this part asks user if they want to search for another city
    while True:
        option = input("\nWant to get report of another place? Y/N \n>>> ").lower()
        if option in ["yes", "y"]:
            break
        elif option in ["no", "n"]:
            print("\nThank you for using my Weather Reporter 😊")
            exit()
        else:
            print("Invalid Input\nTry Again")
