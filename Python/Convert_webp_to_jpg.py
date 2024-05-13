from PIL import Image
import os


dir_path = ""

for image in os.listdir(dir_path):
    img = Image.open(f"{dir_path}\\{image}").convert("RGB")
    img.save(f"{dir_path}\\{image.split('.webp')[0]}.jpg",'jpeg')
    os.remove(f"{dir_path}\\{image}")