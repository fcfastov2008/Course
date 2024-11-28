
import requests
import os


url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)


if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    if not photos:
        print("Фото не знайдено для заданих параметрів.")
    else:
        os.makedirs("mars_photos", exist_ok=True)
        for k, photo in enumerate(photos[:10]):
            img_url = photo.get('img_src')
            if img_url:
                print(f"Завантажую фото {k + 1}: {img_url}")
                img_data = requests.get(img_url).content
                file_name = f"mars_photos/mars_photo{k + 1}.jpg"
                with open(file_name, 'wb') as file:
                    file.write(img_data)

else:
    print(f"Помилка запиту: {response.status_code}")