from PIL import Image, ImageDraw

def create_image(size, cells):
    img = Image.new("RGB", size, color="white")
    drawer = ImageDraw.Draw(img)
    y = 0

    for line in cells:
        x = 0
        for cell in line:
            color = "#FFFFFF" if cell == 1 else "#000000"
            drawer.rectangle([(x, y), (x + 10, y + 10)], fill=color)
            x += 10
        y += 10
    return img

def create_gif(path, size, images):
    dest = Image.new("RGB", size)
    dest.save(path, save_all=True, append_images=images)
