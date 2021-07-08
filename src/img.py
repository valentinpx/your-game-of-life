from PIL import Image, ImageDraw

def createImage(path, cells):
    img = Image.new('RGB', (1120, 520), color = 'white')
    drawer = ImageDraw.Draw(img)
    y = 0

    for line in cells:
        x = 0
        for cell in line:
            color = "#000000" if cell == '1' else "#FFFFFF"
            drawer.rectangle([(x, y), (x + 10, y + 10)], fill=color)
            x += 10
        y += 10
    img.save(path)