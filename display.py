"""
display - 1.69inch LCD Display Module, 240×280 Resolution ST7789V2 https://www.aliexpress.com/item/1005005752009686.html
requires firmware from https://github.com/russhughes/st7789_mpy
"""

import gc
import st7789
import vga2_bold_16x32 as font
from machine import Pin, SPI

gray = 0x4A49

class display:
    def __init__(self) -> None:
        self.tft = st7789.ST7789(SPI(2, baudrate=40000000, sck=Pin(18), mosi=Pin(23)),
            240, 300,
            reset=Pin(4, Pin.OUT),
            cs=Pin(5, Pin.OUT),
            dc=Pin(2, Pin.OUT),
            backlight=Pin(13, Pin.OUT),
            rotation=0, options=0,
            buffer_size=0)
        self.tft.init()
        self.tft.fill(st7789.BLACK)

        self.temp = '.'
        self.in_temp = '.'
        self.out_temp = '.'
        self.mode = '.'
        self.fan = '.'

    def update(self, temp, in_temp, out_temp, mode, fan):
        if temp is '0': temp = '--'
        if in_temp is '0': in_temp = '--'
        if out_temp is '0': out_temp = '--'

        print(f"disp temp {temp} in_temp {in_temp} out_temp {out_temp} mode {mode} fan {fan}")

        gc.collect()
        print(f"a {gc.mem_alloc()} f {gc.mem_free()}")

        #Target temperature
        if mode != self.mode or temp != self.temp:
            self.mode = mode
            self.temp = temp

            if mode == 'HEAT': color = 'r'
            elif mode == 'COOL': color = 'b'
            else: color = 'n'
            name = f"Lfonts/{color}{temp}.png"
            self.tft.png(name, 5,18)

        #Outside temperature
        if out_temp != self.out_temp:
            self.out_temp = out_temp
            name = f"Sfonts/g{out_temp}.png"
            self.tft.png(name, 5, 160)

        #Inside temperature
        if in_temp != self.in_temp:
            self.in_temp = in_temp
            name = f"Sfonts/b{in_temp}.png"
            self.tft.png(name, 125, 160)

        #Fan speed
        if fan != self.fan:
            self.fan = fan
            self.tft.fill_rect(5, 245, 230, 40, st7789.BLACK)
            if fan in ('AUTO', 'QUIET'):
                self.tft.fill_rect(5, 245, 228, 40, gray)
                self.tft.text(font, fan, 25, 250, st7789.WHITE, gray)
            if fan in ('1','2','3','4','5'):
                self.tft.fill_rect(5, 245, 40, 40, gray)
            if fan in ('2','3','4','5'):
                self.tft.fill_rect(52, 245, 40, 40, gray)
            if fan in ('3','4','5'):
                self.tft.fill_rect(99, 245, 40, 40, gray)
            if fan in ('4','5'):
                self.tft.fill_rect(146, 245, 40, 40, gray)
            if fan in ('5'):
                self.tft.fill_rect(193, 245, 40, 40, gray)

        return

    def on(self):
        print("on")
        self.tft.sleep_mode(False)
        self.tft.on()

    def off(self):
        print("off")
        self.tft.sleep_mode(True)
        self.tft.off()
