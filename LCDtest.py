#!/usr/bin/python
# Example using a character LCD plate.
import time
from time import sleep, strftime
from datetime import datetime
import Adafruit_CharLCD as LCD


# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

# create some custom characters
lcd.create_char(1, [2, 3, 2, 2, 14, 30, 12, 0])
lcd.create_char(2, [0, 1, 3, 22, 28, 8, 0, 0])
lcd.create_char(3, [0, 14, 21, 23, 17, 14, 0, 0])
lcd.create_char(4, [31, 17, 10, 4, 10, 17, 31, 0])
lcd.create_char(5, [8, 12, 10, 9, 10, 12, 8, 0])
lcd.create_char(6, [2, 6, 10, 18, 10, 6, 2, 0])
lcd.create_char(7, [31, 17, 21, 21, 21, 21, 17, 31])

# Show button state.
lcd.clear()
lcd.message('Press buttons...')

# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Pellet Pirate V1', (1,1,1)),
            (LCD.LEFT,   'Left - Aye Matey!'  , (1,0,0)),
            (LCD.UP,     'Up'    , (1,0,0)),
            (LCD.DOWN,   'Down'  , (1,0,0)),
            (LCD.RIGHT,  'Right' , (1,1,1)) )

print('Press Ctrl-C to quit.')

try:
    while True:
        # Loop through each button and check if it is pressed.
        for button in buttons:
            if lcd.is_pressed(button[0]):
                # Button is pressed, change the message and backlight.
                lcd.clear()
                lcd.message(button[1] + '\n')
                lcd.message(datetime.now().strftime('%b %d %H:%M:%S'))
                lcd.set_color(button[2][0], button[2][1], button[2][2])
except KeyboardInterrupt:
    lcd.clear()
    lcd.message('Good-bye')
