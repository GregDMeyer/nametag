
import os
from PIL import Image, ImageDraw, ImageFont
from random import choice
from time import sleep

from sys import path
path += ['/home/pi/Code/PaperTTY']
from pipe_driver import AutoPipeDisplay
from IT8951 import constants

def read_file(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            lst.append(line.strip())
    return lst

def generate_name():
    firstnames = read_file('firstnames.csv')
    lastnames = read_file('lastnames.csv')

    return ' '.join([choice(firstnames), choice(lastnames)])

def generate_university():
    universities = read_file('colleges.csv')
    return choice(universities)

def draw_centered_text(text, y, fontsize, img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('BrownBagLunch.ttf', fontsize)
    text_width, _ = font.getsize(text)

    text_x = img.size[0]//2 - text_width//2

    draw.text((text_x, y), text, font=font, fill=(0,0,0,255))

def generate_nametag_image():
    img = Image.open('hello.png')

    draw_centered_text(generate_name(), 250, 120, img)
    draw_centered_text(generate_university(), 420, 50, img)

    return img

def main():
    display = AutoPipeDisplay()

    while True:
        img = generate_nametag_image()
        display.frame_buf.paste(img)
        display.write_partial(constants.DisplayModes.GL16)

        sleep(10)

if __name__ == '__main__':
    main()
