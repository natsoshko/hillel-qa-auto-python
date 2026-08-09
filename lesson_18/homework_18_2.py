import requests

BASE_URL = "http://127.0.0.1:8081"

image_name = "istock_photo.jpg"
# POST file
with open(image_name, "rb") as image:
    files = {"image": image}
    response = requests.post(f"{BASE_URL}/upload", files=files)

print("POST status code:", response.status_code)
print(response.json())

# GET file
headers = {"Content-Type": "text"}
response = requests.get(f"{BASE_URL}/image/{image_name}", headers=headers)

print("\nGET status code:", response.status_code)
print(response.json())

# DELETE file
response = requests.delete(f"{BASE_URL}/delete/{image_name}")

print("\nDELETE статус:", response.status_code)
print(response.json())

# GET again
headers = {"Content-Type": "text"}
response = requests.get(f"{BASE_URL}/image/{image_name}", headers=headers)

print("\nGET status code:", response.status_code)
print(response.json())