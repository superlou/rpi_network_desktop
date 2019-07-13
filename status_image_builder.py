from PIL import Image, ImageDraw, ImageFont
import socket
import fcntl
import struct
import subprocess


class StatusImageBuilder:
    def __init__(self):
        self.font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 110)

    def generate(self, fields, output):
        white = (255, 255, 255)

        image = Image.new('RGBA', (1920, 1080), (0, 0, 0, 255))
        draw = ImageDraw.Draw(image)
        
        spacing = 140
                
        for i, (key, value) in enumerate(fields.items()):
            self.labeled_field(draw, 20, spacing * i + 130, key, value, white, self.font)

        image.save(output, "PNG")

    def labeled_field(self, draw, x, y, name, value, color, font):
        draw.text((x, y), name + ":", fill=color, font=font)
        draw.text((x + 700, y), value, fill=color, font=font)
