import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

FONT_NAME = "Vera.ttf"


class OledDisplay:

    def __init__(self):
        self._display = self._init_display()
        self._font = ImageFont.load_default()
        self._big_font = ImageFont.truetype(FONT_NAME, 20)
        self._font2 = ImageFont.truetype(FONT_NAME, 10)

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

        time_width, time_height = self._font.getsize(time)
        draw.text((2, height - time_height), time, font=self._font, fill=255)

        co2_text = "%d" % co2
        co2_width, _ = self._big_font.getsize(co2_text)
        draw.text((width - co2_width, 0), co2_text, font=self._big_font, fill=255)
        self.draw_co2_label(draw, width - co2_width, 0)

        draw.text((2, 2), "t%.1f" % temp, font=self._font, fill=255)
        draw.text((2, 11), "h%.1f" % humidity, font=self._font, fill=255)

        self._display.image(image)
        self._display.display()

    def draw_co2_label(self, draw, x_offset, y_offset):
        draw.text((x_offset - 19, y_offset + 2), "co2", font=self._font2, fill=255)
        draw.text((x_offset - 23, y_offset + 10), "ppm", font=self._font2, fill=255)