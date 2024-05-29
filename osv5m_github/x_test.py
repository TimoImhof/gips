from PIL import Image
from models.huggingface import Geolocalizer

geolocalizer = Geolocalizer.from_pretrained('osv5m/baseline')
img = Image.open('.media/examples/img1.jpeg')
x = geolocalizer.transform(img).unsqueeze(0) # transform the image using our dedicated transformer
gps = geolocalizer(x) # B, 2 (lat, lon - tensor in rad)

print(gps)

print(geolocalizer)