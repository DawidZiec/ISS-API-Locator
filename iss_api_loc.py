import requests
import os
import time
import folium
from selenium import webdriver

url = "https://api.wheretheiss.at/v1/satellites/25544"
driver = webdriver.Edge()


while(True):
    response = requests.get(url)
    response = response.json()
    os.system('cls')
    print("Aktualna pozycja ISS")
    print("Szerokość geograficzna:", response["latitude"])
    print("Długość geograficzna:", response["longitude"])
    print("Wysokość:", response["altitude"])
    lat = response["latitude"]
    lon = response["longitude"]
    print()

    m = folium.Map(
        location=[lat, lon],
        zoom_start=3
    )

    folium.Marker([lat, lon], tooltip="ISS").add_to(m)

    m.save('index.html')

    driver.get('index.html')
    time.sleep(1)
    driver.refresh()

driver.quit()
