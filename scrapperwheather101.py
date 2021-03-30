import requests
from bs4 import BeautifulSoup

print("Downloading page...")
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=30.504170000000045&lon=-90.45845999999995")
assert page.status_code == 200

print("Parsing HTML...")
soup = BeautifulSoup(page.content, 'html.parser')


print("Extracting temperature...")
temp = soup.find('p', {'class': 'myforecast-current-lrg'}).get_text()


print()
print(f"The temperature is {temp}.")
