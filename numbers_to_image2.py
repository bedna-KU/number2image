import cv2
import numpy as np
import sys
from random import randrange

MAX_COLORS = (256 * 256 * 256) ** 2 - 1

def make_image(red_start, red_end, green_start, green_end, blue_start, blue_end, width):
    pixels_num = width ** 2
    green = green_start
    blue = blue_start
    red = red_start
    
    pixels = []
    for pixel in range(pixels_num):
        green_step = (green_end - green_start) / (pixels_num - 1)
        green += green_step
        blue_step = (blue_end - blue_start) / (pixels_num - 1)
        blue += blue_step
        red_step = (red_end - red_start) / (pixels_num - 1)
        red += red_step
        
        pixels.append([blue - blue_step, green - green_step, red - red_step])

    pixels = np.array(pixels, 'uint8')
    pixels = pixels.reshape(width, width, 3)
    return pixels

def number_to_color(number, max_number):
    number_rgb_color = int(MAX_COLORS / max_number * number)
    return number_rgb_color

def int_rgb_color(n):
    mask = (1 << 8) - 1
    return [(n >> k) & mask for k in range(0, 48, 8)]

def main():
    numbers = []
    number_max = int(sys.argv[1]) + 1
    number_count = int(sys.argv[2]) + 1
    for x in range(1, number_count):
        number = randrange(1, number_max)
        # number = x
        while number in numbers:
            number = randrange(1, number_max)
        numbers.append(number)
        number_color = number_to_color(number, number_max)
        print(">>>", x, number, number_color)
        number_rgb_color = int_rgb_color(number_color)
        print("---", number_rgb_color)
        image = make_image(
                            number_rgb_color[2],
                            number_rgb_color[5],
                            number_rgb_color[1],
                            number_rgb_color[4],
                            number_rgb_color[0],
                            number_rgb_color[3],
                            8)
        if x > 1:
            image_prev = np.concatenate((image_prev, image), axis=1)
        else:
            image_prev = image

    cv2.imshow("Image", image_prev)
    cv2.waitKey()

if __name__ == '__main__':
    image = main()