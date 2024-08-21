## @file Display.py
#  @title Display
#  @brief A dispay option to display the generated flag.
#  @author Ganghoon Park
#  @date 2022-04-11

import cv2
import glob
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import FlagGenerator
import HashGenerator
import GUI
from subprocess import call

## @brief FlagDisplay is a class that allows the user to generate and display
#         the flag.
#  @details the FlagDisplay contains the text input box,
#           generate button, back button.
#           display button, and a clear button for the user to use.


class FlagDisplay(Frame):

    ## @brief Creates the next page after clicking
    #         the start button from the GUI main page.
    #  @details The GUI second page will have the text input box,
    #           generate button, display button, and a back button.
    #  @param self Current object, common
    #         first parameter for any method of a class.
    #  @param parent A widget that acts as the parent of self, current object.
    #         All widgets in tkinter except the root window require a parent
    #  @param controller Other objects that are designed to act as a shared
    #         point, allowing several pages of widgets to interact. It
    #         decouples the different pages, making them independent. The
    #         controller descides what page will be visible.
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.FG = FlagGenerator.FlagGenerator()

        self.image_text_input = Image.open("./ImagesGUI/text_input.png")
        self.image_generate_button = Image.open(
            "./ImagesGUI/generate_button.png")
        self.image_display_button = Image.open(
            "./ImagesGUI/display_button.png")
        self.image_back_button = Image.open("./ImagesGUI/back_button.png")
        self.image_clear_button = Image.open("./ImagesGUI/clear_button.png")

        self.resize_image_text_input = self.image_text_input.resize((600, 120))
        self.resize_generate_button = self.image_generate_button.resize(
            (200, 100))
        self.resize_image_display_button = self.image_display_button.resize(
            (200, 100))
        self.resize_image_back_button = self.image_back_button.resize(
            (200, 100))
        self.resize_image_clear_button = self.image_clear_button.resize(
            (200, 100))

        self.photo_text_input = ImageTk.PhotoImage(
            self.resize_image_text_input)
        self.photo_generate_button = ImageTk.PhotoImage(
            self.resize_generate_button)
        self.photo_display_button = ImageTk.PhotoImage(
            self.resize_image_display_button)
        self.photo_back_button = ImageTk.PhotoImage(
            self.resize_image_back_button)
        self.photo_clear_button = ImageTk.PhotoImage(
            self.resize_image_clear_button)

        self.label = Label(self, image=self.photo_text_input)

        self.button_generate = Label(self, image=self.photo_generate_button)
        self.button_generate.bind("<Button 1>", self.generate)
        self.generate = Button(self, text="Generate", command=self.generate)

        self.val = StringVar()

        self.button_display = Label(self, image=self.photo_display_button)
        self.button_display.bind("<Button 1>", self.display)
        self.display = Button(self, text="Display", command=self.display)

        self.val = StringVar()

        self.button_back = Button(
            self, image=self.photo_back_button,
            command=lambda: controller.show_frame("StartPage"))
        self.button_back.bind(
            "<Button 1>", lambda self: controller.show_frame("StartPage"))

        self.button_clear = Label(self, image=self.photo_clear_button)
        self.button_clear.bind("<Button 1>", self.delete_image)
        self.delete_image = Button(
            self, text="Back", command=self.delete_image)

        self.input_box = Entry(self, width=30, font=('Arial 24'))

        self.init_window()

    ## @brief Places the different widgets onto the second page after
    #   clicking on the start button on the GUI main page.
    #  @details The second page will include the text input input box,
    #   generate button, display button, clear button, and a back button.
    def init_window(self):

        self.label.place(x=95, y=100)
        self.input_box.place(x=125, y=250)
        self.button_generate.place(x=145, y=350)
        self.button_display.place(x=445, y=350)
        self.button_back.place(x=145, y=475)
        self.button_clear.place(x=445, y=475)

    ## @brief Gets the input string from the input text box
    #  @details The input string is retrieved with this function
    def get_input_string(self):
        global input_string
        input_string = self.input_box.get()
        return input_string

    ## @brief Generates the flag from the input string
    #  @details The flag is generated with this function
    #  @param event When generate button is clicked,
    #   it will call this function to generate the flag.
    def generate(self, event):
        self.FG.generate_flag(self.get_input_string())

    ## @brief Displays the generated flag
    #  @details The generated flag is displayed
    #   on the screen with this function
    #  @param event When display button is clicked,
    #   it will call this function to display the flag.
    def display(self, event):
        self.image_display = Image.open(
            "./generated_flags/flag_"+self.get_input_string()+".png")
        self.resized_image_display = self.image_display.resize((660, 440))
        self.photo_display = ImageTk.PhotoImage(self.resized_image_display)
        self.label_display = Label(self, image=self.photo_display)
        self.label_display.place(x=65, y=10)

        self.image_empty = Image.open("./ImagesGUI/empty.png")
        self.resized_image_empty = self.image_empty.resize((220, 120))
        self.photo_empty = ImageTk.PhotoImage(self.resized_image_empty)
        self.label_empty = Label(self, image=self.photo_empty)
        self.label_empty.place(x=145, y=475)

    ## @brief Clears the displayed flag
    #  @details The generated flag is cleared on the screen with this function
    #  @param event When clear button is clicked,
    #   it will call this function to clear the flag being displayed.
    def delete_image(self, event):
        self.label_display.destroy()
        self.label_empty.destroy()
