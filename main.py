import cv2
import image_dehazer
import tkinter
import os
import sys
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import math

def ssim(img1, img2):
    # Convert images to grayscale
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calculate mean, variance, and covariance
    k1 = 0.01
    k2 = 0.03
    L = 255  # Dynamic range of the images
    C1 = (k1 * L) ** 2
    C2 = (k2 * L) ** 2
    mu1 = cv2.GaussianBlur(img1_gray, (11, 11), 1.5)
    mu2 = cv2.GaussianBlur(img2_gray, (11, 11), 1.5)
    mu1_sq = mu1 ** 2
    mu2_sq = mu2 ** 2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.GaussianBlur(img1_gray ** 2, (11, 11), 1.5) - mu1_sq
    sigma2_sq = cv2.GaussianBlur(img2_gray ** 2, (11, 11), 1.5) - mu2_sq
    sigma12 = cv2.GaussianBlur(img1_gray * img2_gray, (11, 11), 1.5) - mu1_mu2

    # Calculate SSIM
    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))-1
    ssim_index = np.mean(ssim_map)

    return ssim_index

def open_image():
    global img
    global img_name
    global submit
    global HazeImg

    img_name=filedialog.askopenfilename(initialdir=",", title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")])

    HazeImg = cv2.imread(img_name) # Covert to Matrices
    input.insert(0, img_name)

    l1 = tkinter.Label(root, text="Original Image:")
    l1.grid(column=0, row=2)

    img1 = Image.open(img_name)

    width, height = img1.size
    if  (width > 1200 or height > 1200):
        img = ImageTk.PhotoImage(Image.open(img_name).resize((width // 5,height // 5)))
    elif (width < 800 or height < 800):
        img = ImageTk.PhotoImage(Image.open(img_name).resize((width ,height)))
    else:
        img = ImageTk.PhotoImage(Image.open(img_name).resize((width //2,height/2)))

    l2 = tkinter.Label(root, image=img)
    l2.grid(column=0, row=3)

    submit = tkinter.Button(root, text="Submit", command=call_haze)
    submit.grid(column=2, row=1)

def call_haze():
    global dehazed,Hmap_img

    submit.destroy()
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(HazeImg, showHazeTransmissionMap=False)

    mse = np.mean((HazeImg - HazeCorrectedImg) ** 2) 
    if(mse == 0): 
        print(100)
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse)) 
    print("Peak Signal to Noise Ratio(PSNR) : ",psnr)

#SSIM 
    ssim_index = ssim(HazeImg, HazeCorrectedImg)
    print("SSIM Index:",ssim_index)

    cv2.waitKey(0)
    cv2.imwrite("outputImages/res1.png", HazeCorrectedImg)
    cv2.imwrite("outputImages/hazemap.png", haze_map)
    cv2.imshow('haze_map', haze_map)

    msg = tkinter.Label(root, text="Dehazing complete! Image stored in dehazed folder.")
    msg.grid(column=0, row=4, columnspan=2)

    l3=tkinter.Label(root, text="Dehazed Image:")
    l3.grid(column=1, row=2)
    
    img1 = Image.open("outputImages/res1.png")  

    width, height = img1.size

    if  (width > 1200 or height > 1200):
        dehazed = ImageTk.PhotoImage(Image.open('outputImages/res1.png').resize((width // 5,height // 5)))
    elif (width < 800 or height < 800):
        dehazed = ImageTk.PhotoImage(Image.open('outputImages/res1.png').resize((width ,height)))
    else:
        dehazed = ImageTk.PhotoImage(Image.open('outputImages/res1.png').resize((width // 2 ,height // 2)))

    
    l4 = tkinter.Label(root, image=dehazed)
    l4.grid(column=1, row=3, padx=10)

    retry = tkinter.Button(root, text="Retry", command=restart_program)
    retry.grid(column=0, row=5)

    quit = tkinter.Button(root, text="Quit", command=quit_program)
    quit.grid(column=1, row=5)

def restart_program():
    os.execl(sys.executable, sys.executable, *sys.argv)

def quit_program():
    sys.exit()

root = tkinter.Tk()
root.geometry("1920x1080+0+0")
root.title = "Dehaze"
root.update_idletasks()

label = tkinter.Label(root, text="Select image or enter Image path:")
label.grid(column=0, row=0)

input = tkinter.Entry(root, width=50)
input.grid(column=0)

browse = tkinter.Button(root, text="Browse", command=open_image)
browse.grid(column=1, row=1)

root.mainloop()