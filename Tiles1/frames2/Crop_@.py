from PIL import Image
from pathlib import Path

img = Image.open('Tileset.png')
path = Path.cwd() / "frames"

print(type(path))
counter = 0 
for fila in range(0,16):
    if fila < 4:
        n = 32
    else:
        n = 16
        
    y = fila*16
    y2 = y+n
    for columna in range(0,16):
        x = columna*16
        x2 = x + 16
        crop_img = img.crop((x,y,x2,y2))
        crop_img.save(f"tile{counter}.png")
        counter+=1


    
