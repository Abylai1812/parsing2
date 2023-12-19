import requests
from bs4 import BeautifulSoup

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 7.1; Xperia V Build/NDE63X) AppleWebKit/600.3 (KHTML, like Gecko)  Chrome/55.0.2635.298 Mobile Safari/533.5',
}

for i in range(1, 4):
    print(f"Парсим {i} страницу")
    url = f"https://www.olx.kz/list/q-%D0%B5%D0%BB%D0%BA%D0%B8/?page={i}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    cards = soup.find_all("div", class_="css-1sw7q4x")

    for card in cards:
        listing_url = f"https://www.olx.kz/{card.a['href']}"
        listing_response = requests.get(listing_url, headers=headers)
        listing_soup = BeautifulSoup(listing_response.text, "lxml")

        description = listing_soup.find("div", class_="css-1t507yq er34gjf0")

        if description:
            print(description.text.strip())
        else:
            print("Описание не найдено")
