## @file Gallery.py
#  @title Gallery
#  @brief A gallery to showcase all the generated flags.
#  @author Ganghoon Park
#  @date 2022-04-11

import cv2
import glob
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import GUI
import Help
from subprocess import call

## @brief FlagGallery is a class that opens the gallery so that the user
#         can look at the generated flags.
#  @details the FlagGallery contains the open gallery button and a back button
#           for the user to control.


class FlagGallery(Frame):

    ## @brief Constructor for FlagGallery GUI object
    #  @details Creates object for GUI
    #  @param *args allows the function
    #          to accept an arbitrary number of arguments
    #  @param **kwargs allows the function to
    #         accept an arbitrary number of keyword arguments.
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.image_back_button = Image.open("./ImagesGUI/back_button.png")
        self.resize_image_back_button = self.image_back_button.resize(
            (200, 100))
        self.photo_back_button = ImageTk.PhotoImage(
            self.resize_image_back_button)
        self.button_back = Button(
            self, image=self.photo_back_button,
            command=lambda: controller.show_frame("StartPage"))
        self.button_back.bind(
            "<Button 1>", lambda self: controller.show_frame("StartPage"))

        self.image_open_gallery_button = Image.open(
            "./ImagesGUI/open_gallery_button.png")
        self.resize_image_open_gallery_button = (
                                        self.image_open_gallery_button.resize(
                                         (400, 200)))
        self.photo_open_gallery_button = ImageTk.PhotoImage(
            self.resize_image_open_gallery_button)
        self.button_open_gallery = Button(self,
                                          image=(
                                           self.photo_open_gallery_button),
                                          command=self.open_gallery)

        self.init_window()

    ## @brief method for placing buttons in FlagGallery.
    #  @details the buttons will be placed onto the FlagGallery GUI.
    def init_window(self):
        self.button_open_gallery.place(x=200, y=125)
        self.button_back.place(x=295, y=475)

    ## @brief method for open the gallery after
    #        clicking the open gallery button.
    #  @details it will close the FlagGallery frame
    #           and open the gallery window.
    def open_gallery(self):
        self.controller.destroy()
        self.open_gallery_win()

    ## @brief method for constructing the gallery.
    #  @details it will showcase all the generated flags by clicking buttons
    #           for next and previous flag.
    def open_gallery_win(self):
        gallery_win = Tk()
        gallery_win.title('Gallery Window')
        gallery_win.geometry("800x600")
        gallery_win.resizable(0, 0)

        panel = tk.Label(gallery_win)
        panel.pack()
        path = "generated_flags/*.*"
        images = glob.glob(path)
        flag = iter(images)

        list1 = []

        global counter
        counter = -1

        for name in glob.glob(path):
            list1.append(name)

        text = tk.StringVar()
        text.set(list1[counter])
        label = Label(textvariable=text)
        label.pack()

        ## @brief method for incrementing the counter and showing the next flag
        #  @details the global variable counter is updated
        #           every time next flag is clicked
        def inc_count():
            global counter
            counter += 1
            if counter == len(list1):
                counter = 0
            next_flag(counter)
            print_flag_name()

        ## @brief method for decrementing the counter
        #        and showing the previous flag
        #  @details the global variable counter is updated
        #           every time previous flag is clicked
        def dec_count():
            global counter
            counter -= 1
            if -counter == len(list1):
                counter = 0
            previous_flag(counter)
            print_flag_name()

        ## @brief method for displaying the next flag
        #  @details the next flag in the list is opened and resized.
        #           Then, it is displayed.
        #  @param counter a global integer variable to keep track of the image.
        def next_flag(counter):

            try:
                img = list1[counter]
            except StopIteration:
                return

            img = Image.open(img)
            resized_img = img.resize((660, 440))
            img = ImageTk.PhotoImage(resized_img)

            panel.img = img
            panel['image'] = img

        ## @brief method for displaying the previous flag
        #  @details the previous flag in the list is opened and resized.
        #           Then, it is displayed.
        #  @param counter a global integer variable to keep track of the image.
        def previous_flag(counter):
            ab = list1[counter]
            img = Image.open(ab)
            resized_img = img.resize((660, 440))
            img = ImageTk.PhotoImage(resized_img)

            panel.img = img
            panel['image'] = img

        ## @brief method for returning to the main menu
        #  @details once it is clicked, it closes the gallery window
        #           and opens the main start page.
        def return_menu():
            gallery_win.destroy()
            call(["python", "GUI.py"])

        ## @brief method for displaying the flag name
        #  @details the name of the flag is displayed.
        def print_flag_name():
            text.set(list1[counter])

        next_flag_btn = tk.Button(text='Next Flag', command=inc_count)
        previous_flag_btn = tk.Button(text='Previous Flag', command=dec_count)
        return_menu_btn = Button(
            text='Return to Main Menu', command=return_menu)

        next_flag_btn.pack()
        previous_flag_btn.pack()
        return_menu_btn.pack()

        inc_count()

        gallery_win.mainloop()
