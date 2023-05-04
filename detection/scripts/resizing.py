from PIL import Image
import os
from os import listdir


directory = 'crops'

for filename in listdir(directory):
    file  = os.path.join(directory, filename)
    image = Image.open(file)
    new_image = image.resize((640, 640), 0)
    new_image.save('resized/'+filename+'resized.jpg')







