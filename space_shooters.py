#!/usr/bin/env python3
# Created by: Gustav I
# Created on: May 28, 2025
# This is the program for "Space shooters"

import ugame
import stage


def game_scene():
    # this function is the main game scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers of all sprites, items show up in order
    game.layers = [ship] + [background]
    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()
    print("Welcome to Space Shooters")

    # repeat forever, game loop
    while True:
        # Get user input

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
