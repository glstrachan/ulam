import sys
import argparse
import math
import numpy as np

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path

from PIL import Image, ImageDraw


def generate(size): #Generates an Ulam spiral array
    if size % 2 != 1:
        print("Unable to perform generation\nInvalid Size")
        return 0

    iteration = 0

    A = np.full([size, size], 0) #Initialize empty array with dimensions side * side

    x = int(size / 2)
    y = x
    step = 0

    for z in range(size + 1):
        if step == 2:
            step = 0

        if step == 0:
            for i in range(z):

                check = iteration - 1
                if prime(check) == True:
                    A[x][y] = 1

                y = y + 1
                iteration = iteration + 1

            for i in range(z):

                check = iteration - 1
                if prime(check) == True:
                    A[x][y] = 1

                x = x + 1
                iteration = iteration + 1

        elif step == 1:
            for i in range(z):

                check = iteration - 1
                if prime(check) == True:
                    A[x][y] = 1

                y = y - 1
                iteration = iteration + 1

            for i in range(z):

                check = iteration - 1
                if prime(check) == True:
                    A[x][y] = 1

                x = x - 1
                iteration = iteration + 1

        step = step + 1
    transfer(A)


def prime(num): #Determines if any given input num is prime
    if num < 2:
        return 0

    prime = True

    for x in range(int(math.sqrt(num)) - 1):
        if num % (x + 2) == 0:
            prime = False

    return prime


def transfer(A):  #Saves the Ulam spiral as an image
    px = 25
    size = len(A)

    img = Image.new('RGB', (size * px, size * px), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)

    R = 1
    G = 1
    B = 1

    for x in range(len(A)):
            for y in range(len(A)):
                if A[x][y] == 1:
                    draw.rectangle([y * px, x * px, (y + 1) * px, (x + 1) * px], fill = (int(17 * R * R/6), int(50 * G * G/4), int(18 * B * B/6)), outline = None, width = 1)

                    R = R - 0.0005/len(A) * len(A)
                    G = G + 0.001/len(A) * len(A)
                    B = B - 0.0005/len(A) * len(A)

    img.save(dir_path + '\spiral.jpg')


def show(A): #Draws a given array A
    for x in range(len(A)):
        for y in range(len(A)):
            print(A[x][y], end =" ")
        print("")
    print("", end="\n")

num = int(input("Enter a sidelength\nNumbers exceeding 1000 can take a while to generate\n"))
generate(num)
