## @file Help.py
#  @title Help
#  @brief A help option teach the user how to use the software
#         and giving more information of it.
#  @author Ganghoon Park
#  @date 2022-04-11

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import FlagGenerator
import HashGenerator

## @brief Shows the help menu to teach the user how to use the software and
#         how it works.
#  @details The help menu will have instructions and a button to go back to
#           the main GUI screen.


class Help(Frame):

    ## @brief Creates the help page after
    #         clicking the help button from the GUI main page.
    #  @details The help page will have the instructions and a back button.
    #  @param self Current object, common first parameter
    #         for any method of a class.
    #  @param parent A widget that acts as the parent of self, current object.
    #         All widgets in tkinter except the root window require a parent
    #  @param controller Other objects that are designed to act as a shared
    #         point, allowing several pages of widgets to interact. It
    #         decouples the different pages, making them independent. The
    #         controller descides what page will be visible.
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

        self.image = Image.open("./ImagesGUI/instructions.png")
        self.resized_image = self.image.resize((500, 400))
        self.photo = ImageTk.PhotoImage(self.resized_image)
        self.label = Label(self, image=self.photo)

        self.init_window()

    ## @brief Places the different widgets onto the help page
    #         after clicking on the help button on the GUI main page.
    #  @details The help page will include the instructions and a back button.
    def init_window(self):
        self.label.place(x=130, y=20)
        self.button_back.place(x=295, y=475)
