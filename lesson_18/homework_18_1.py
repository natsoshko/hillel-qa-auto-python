import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

response = requests.get(search_url, params = search_params)
status_code = response.status_code
search_data = response.json()

print("status_code:", status_code)
print("response_json", search_data)

items = search_data["collection"]["items"]
nasa_ids = []

for item in items:
    data = item["data"][0]
    # print(data)
    nasa_id = data["nasa_id"]
    nasa_ids.append(nasa_id)

    if len(nasa_ids) == 5:
        break
print("NASA IDs:", nasa_ids)

index = 1
for nasa_id in nasa_ids:
    asset_url_template = f"{BASE_URL}/asset/{nasa_id}"
    asset_response = requests.get(asset_url_template)
    asset_data = asset_response.json()
    jpg_url = None

    for item in asset_data["collection"]["items"]:
        href = item["href"]
        if href.lower().endswith("small.jpg"):
            jpg_url = href
            break

    if jpg_url is None:
        print(f"Для {nasa_id} JPG не знайдено.")
        continue

    filename = f"mars_photo{index}.jpg"
    index += 1

    image_response = requests.get(jpg_url)

    with open(filename, "wb") as file:
        file.write(image_response.content)

    print("Image", filename, "is saved")
