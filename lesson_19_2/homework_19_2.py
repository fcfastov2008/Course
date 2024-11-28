import requests


base_url = "http://127.0.0.1:8080"


upload_url = f"{base_url}/upload"
file_path = "example.jpg"
with open(file_path, "rb") as file:
    files = {"image": file}
    response = requests.post(upload_url, files=files)
    if response.status_code == 201:
        print("Зображення успішно завантажено!")
        image_url = response.json().get("image_url")
        print(f"URL зображення: {image_url}")
    else:
        print("Помилка при завантаженні зображення:", response.text)
        exit()


filename = image_url.split("/")[-1]
get_image_url = f"{base_url}/image/{filename}"
response = requests.get(get_image_url, headers={"Content-Type": "text"})
if response.status_code == 200:
    print("URL для отримання зображення:", response.json().get("image_url"))
else:
    print("Помилка при отриманні зображення:", response.text)


delete_url = f"{base_url}/delete/{filename}"
response = requests.delete(delete_url)
if response.status_code == 200:
    print("Зображення успішно видалено:", response.json().get("message"))
else:
    print("Помилка при видаленні зображення:", response.text)
