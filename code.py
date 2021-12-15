import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import os
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306

# TODO - put if(btn?.value) in a method

WIDTH = 128
HEIGHT = 32
CENTER_X = int(WIDTH/2)
CENTER_Y = int(HEIGHT/2)

displayio.release_displays()

SDA = board.GP8
SCL = board.GP9
i2c = busio.I2C(SCL, SDA)

display_bus = displayio.I2CDisplay(i2c, device_address=60)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)


# PROFILE SWITCHER
btn1_pin = board.GP16

btn2_pin = board.GP15
btn3_pin = board.GP14

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

profile = 1
print(" profile:", profile, ":)")
while True:
    if btn1.value: # SWITCH_PROFILE
        if(profile < 2):
            profile = profile + 1 # profile++ ?
        else:
            profile = 1
        print("----------------")
        print(" profile:", profile, ":)")
        led.value = True
        time.sleep(0.1)
        led.value = False
    
    if (profile == 1): 
        if btn2.value: # CTRL+ALT+DEL
            print("----------------")
            time.sleep(0.1)
            print(" CTRL+ALT+DEL")
            keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
            led.value = True
            time.sleep(0.1)
            led.value = False
            keyboard.release(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
        
        if btn3.value: # WINDOWS+TAB
            print("----------------")
            time.sleep(0.1)
            print(" Windows+TAB")
            keyboard.press(Keycode.GUI, Keycode.TAB)
            led.value = True
            time.sleep(0.1)
            led.value = False
            keyboard.release(Keycode.GUI, Keycode.TAB)
        
    if (profile == 2): 
        if btn2.value: # COPY(CTRL+C)
            print("----------------")
            time.sleep(0.1)
            print(" copy")
            keyboard.press(Keycode.CONTROL, Keycode.C)
            led.value = True
            time.sleep(0.1)
            led.value = False
            keyboard.release(Keycode.CONTROL, Keycode.C)
        
        if btn3.value: # PASTE(CTRL+V)
            print("----------------")
            time.sleep(0.1)
            print(" paste")
            keyboard.press(Keycode.CONTROL, Keycode.V)
            led.value = True
            time.sleep(0.1)
            led.value = False
            keyboard.release(Keycode.CONTROL, Keycode.V)
        
    time.sleep(0.1)

