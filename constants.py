# !/usr/bin/env python3
# Created by: Gustav I
# Created on: July 2020
# This constants file is for Space Aliens game

# PyBadge screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
FPS = 60
SPRITE_MOVEMENT_SPEED = 2

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}
# new pallet for red filled text
RED_PALETTE = (
    b"\xff\xff\x00\x22\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
