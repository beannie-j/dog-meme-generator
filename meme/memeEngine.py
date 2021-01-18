import os
import sys
from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    def __init__(self, path):
        self.path = path
        self.id = 1

        if not os.path.exists(path):
            os.makedirs(path)

    def make_meme(self, img_path, text, author, scale=500) -> str:
        print("make meme", text, author)

        out = os.path.join(self.path, f"meme-{self.id}.jpg").replace("\\", "/")
        self.id += 1

        img = Image.open(img_path)
        width, height = img.width, img.height
        scale_x = scale // width
        scale_y = scale // height
        resized_img = img.resize((int(scale_x * width), int(scale_y * height)))

        fnt = ImageFont.truetype(
            "./resource/fonts/CircularStd-Book.woff", size=20)

        # drawing context
        d = ImageDraw.Draw(resized_img)
        d.multiline_text(
            (10, 10), f"{text} - {author}", font=fnt, fill=(0, 0, 0, 0))

        resized_img.save(out, 'JPEG')
        return out
