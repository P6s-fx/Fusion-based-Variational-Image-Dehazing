import cv2
import image_dehazer
import tkinter
import os
import sys
from tkinter import filedialog
from PIL import Image, ImageTk

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

    img = ImageTk.PhotoImage(Image.open(img_name).resize((width // 5,height // 5)))
    # img = ImageTk.PhotoImage(Image.open(img_name))
    l2 = tkinter.Label(root, image=img)
    l2.grid(column=0, row=3)

    submit = tkinter.Button(root, text="Submit", command=call_haze)
    submit.grid(column=2, row=1)

def call_haze():
    global dehazed

    submit.destroy()

    # subprocess.call(f"python haze_removal.py \"{img_name}\"",shell=True)
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(HazeImg, showHazeTransmissionMap=False)
    # print(HazeCorrectedImg)

    cv2.waitKey(0)
    cv2.imwrite("outputImages/res1.png", HazeCorrectedImg)

    msg = tkinter.Label(root, text="Dehazing complete! Image stored in dehazed folder.")
    msg.grid(column=0, row=4, columnspan=2)

    l3=tkinter.Label(root, text="Dehazed Image:")
    l3.grid(column=1, row=2)
    
    img1 = Image.open("outputImages/res1.png") 
    width, height = img1.size

    dehazed = ImageTk.PhotoImage(Image.open('outputImages/res1.png').resize((width // 5,height // 5)))
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
# input.grid(column=0, row=1, padx=800, pady=10)
input.grid(column=0)

browse = tkinter.Button(root, text="Browse", command=open_image)
browse.grid(column=1, row=2)

root.mainloop()