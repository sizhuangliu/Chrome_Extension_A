from PIL import Image
import numpy as np

im8 = Image.open('images/design.png')
im8 = im8.resize((int(19),int(19)),Image.ANTIALIAS)
im8.save('images/icon.png', 'PNG')