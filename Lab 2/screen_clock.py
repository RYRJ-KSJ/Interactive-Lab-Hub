import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
<<<<<<< HEAD
from datetime import datetime
from time import strftime, sleep
=======
>>>>>>> b4f31bcf6c9d48655b13298e331b4c0ee4919ec7

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
<<<<<<< HEAD
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)

#image reformation
def image_reform(image1, width, height):
    image1 = image1.convert('RGB')
    image1 = image1.resize((240, 135), Image.BICUBIC)

    return image1
=======
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

>>>>>>> b4f31bcf6c9d48655b13298e331b4c0ee4919ec7
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

<<<<<<< HEAD
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

=======
>>>>>>> b4f31bcf6c9d48655b13298e331b4c0ee4919ec7
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
<<<<<<< HEAD
    x, y = 6, 12
    if buttonA.value and buttonB.value:  # without any button pressed
        image1 = Image.open("dali.jpg")
        image1 = image_reform(image1, width, height)

        draw = ImageDraw.Draw(image1)

        draw.text((90, 15), "Dali Clock", font=font, fill="#000000")


    elif buttonB.value and not buttonA.value:  # press button A
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, y), "Time Stopped", font=font, fill="#FFFFFF")


    elif buttonA.value and not buttonB.value:  # press button B

        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((0, 20), "Time Flies", font=font_small, fill="#FFFFFF")
        draw.text((30, 60), strftime("%H:%M:%S%p"), font=font, fill="#FFFFFF")

    # Display image.
    disp.image(image1, rotation)
    time.sleep(2)
=======

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
>>>>>>> b4f31bcf6c9d48655b13298e331b4c0ee4919ec7
