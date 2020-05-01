import PIL
from PIL import Image, ImageEnhance, ImageFilter
from IPython.display import display
file = "basic.jpg"
img = Image.open(file).convert("RGB")

images=[] 
for shade in range(10,1,-4):
    layer = Image.new('RGB', img.size, color=(0,255,255))
    output = Image.blend(img, layer, shade/30)
    images.append(output)
for shade in range(10,1,-4):
    layer = Image.new('RGB', img.size, color=(255,0,255))
    output = Image.blend(img, layer, shade/30)
    images.append(output)
for shade in range(10,1,-4):
    layer = Image.new('RGB', img.size, color=(255,255,0))
    output = Image.blend(img, layer, shade/30)
    images.append(output)    
    
x=0
y=0
contact_sheet=PIL.Image.new(img.mode, (3*img.width,3*img.height))
for insert in images:
    contact_sheet.paste(insert,(x,y))
    if x+img.width == contact_sheet.width:
        x=0
        y=y+img.height
    else:
        x=x+img.width

contact_sheet=contact_sheet.resize((1200,750))
display(contact_sheet)



