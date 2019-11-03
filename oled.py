import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

FONT_NAME = "/home/pi/programming/serial/VCR.ttf"


class OledDisplay:

    def __init__(self):
        self._display = self._init_display()
        self._font_28 = ImageFont.truetype(FONT_NAME, 28)
        self._font_16 = ImageFont.truetype(FONT_NAME, 16)
        self._font_12 = ImageFont.truetype(FONT_NAME, 12)

    @staticmethod
    def _init_display():
        display = Adafruit_SSD1306.SSD1306_128_64(rst=24)
        display.begin()
        display.clear()
        display.display()
        return display

    def update(self, time, co2, temp, humidity):
        width = self._display.width
        height = self._display.height
        image = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image)

        draw.text((0, 40), time, font=self._font_28, fill=255)

        co2_text = "%04d" % co2
        draw.text((65, -4), co2_text, font=self._font_28, fill=255)

        draw.text((44, 0), "co2", font=self._font_12, fill=255)
        draw.text((44, 9), "PPM", font=self._font_12, fill=255)

        self._draw_block(draw, (13, 18), temp, "C")
        self._draw_block(draw, (74, 18), humidity, "H")

        self._display.image(image)
        self._display.display()

    def _draw_block(self, draw, point, value, mark):
        draw.text(point, "%02d" % value, font=self._font_28, fill=255)
        draw.text((point[0] + 34, point[1] + 11), ("%.1f" % value)[-1:], font=self._font_16, fill=255)
        draw.text((point[0] + 35, point[1] + 2), mark, font=self._font_12, fill=255)
        draw.point((point[0] + 32, point[1] + 23), 255)
