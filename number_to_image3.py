import cv2
import numpy as np
import sys
from random import randrange

MAX_COLORS = 256 * 256 * 256 - 1

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
    return [(n >> k) & mask for k in range(0, 24, 8)]

def main():
    number_start = int(sys.argv[1])
    number_end = int(sys.argv[2])
    number_max = int(sys.argv[3]) + 1
    number_start_for_color = number_to_color(number_start, number_max)
    print(">>>", number_start_for_color)
    number_start_rgb_color = int_rgb_color(number_start_for_color)
    print(">>>", number_start_rgb_color)
    number_end_for_color = number_to_color(number_end, number_max)
    print(">>>", number_end_for_color)
    number_end_rgb_color = int_rgb_color(number_end_for_color)
    print(">>>", number_end_rgb_color)
    image = make_image(
                        number_start_rgb_color[2],
                        number_end_rgb_color[2],
                        number_start_rgb_color[1],
                        number_end_rgb_color[1],
                        number_start_rgb_color[0],
                        number_end_rgb_color[0],
                        8)
    cv2.imshow("image", image)
    cv2.waitKey()

if __name__ == '__main__':
    image = main()