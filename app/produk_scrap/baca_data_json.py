import json

#buka file json
file_json = open("tokopedia.json")

data = json.loads(file_json.read())

print(f"Nama Produk: {data['name']}")
print(f"Harga: {data['price']}")
print(f"Gambar : {data['images']}")
print(f"Link : {data['productLink']}")