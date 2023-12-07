import argparse
import sys
import cv2
import numpy
import numpy as np
import time as clock
from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance

def menu():
     print("the list you can do to this image\n"
          "O : Opening and showing a color input image\n"
          "g : Converting the image to gray-scale\n"
          "+,- : Modifying the brightness (increasing and decreasing\n"
          "c : Improving the contrast\n"
          "t : Thresholding\n"
          "s : Saving the processed image!!\n"
          "Enter your choose:\n")
menu()

is_gray = False
result = aya_img = cv2.imread('dream.jpg', 1)
key = input()
while (True):

    # original image
    if(key=='o' or key=='O'):
        aya_img = cv2.imread('dream.jpg', 1)
        cv2.imshow('dream', aya_img)
        cv2.waitKey(50)
        result = aya_img

    # convert to gray image
    elif (key == "g" or key == "G"):
        is_gray=True
        gray_scale_effect = cv2.cvtColor(aya_img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('dream', gray_scale_effect)
        cv2.waitKey(50)
        result = gray_scale_effect



    # convert to contrast image
    elif (key == 'c' or key == 'C'):
        alpha = 0
        beta = 1.2
        contrast_effect = cv2.normalize(result, None, alpha, beta , norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        cv2.imshow('dream', contrast_effect)
        cv2.waitKey(50)
        result = contrast_effect

   #brighntness
    elif (key == "+"):
        x=255
        y=0.5
        increse_brightness = np.array((x * (result / x) ** y), dtype='uint8')
        cv2.imshow('dream', increse_brightness)
        cv2.waitKey(50)
        result = increse_brightness


    elif (key == '-'):
        c=255
        v=2.5
        less_brightness = np.array(c * (result / c) ** v, dtype='uint8')
        cv2.imshow('dream', less_brightness)
        cv2.waitKey(50)
        result = less_brightness

    #thresholding
    elif (key == 't' or key == 'T'):
        gray_effect = cv2.cvtColor(aya_img, cv2.COLOR_BGR2GRAY)
        thresholding = cv2.adaptiveThreshold(gray_effect, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
        cv2.imshow('dream', thresholding)
        cv2.waitKey(50)
        result = thresholding


    #saving image
    elif (key == 's' or key == 'S'):
        RESULT=result
        cv2.imwrite('RESULT.jpg', result)
        cv2.waitKey(50)

   # another char
    else:
        print("Invalid charachter, you're out. ")
        break;

    key = input()