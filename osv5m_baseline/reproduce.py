from PIL import Image
from b_model.models.huggingface import Geolocalizer

geoloc = Geolocalizer.from_pretrained('osv5m/baseline')
img = Image.open('b_model/.media/examples/img1.jpeg')
x = geoloc.transform(img).unsqueeze(0) # transform the image using our dedicated transformer
gps = geoloc(x) # B, 2 (lat, lon - tensor in rad)

print(gps)