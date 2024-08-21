## @file GUI.py
#  @title GUI
#  @brief A graphical user interface module uses all other modules to allow
#         the user to communicate with the Random Flag Generator software
#  @author Ganghoon Park
#  @date 2022-04-11

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import glob
import FlagGenerator, HashGenerator, Display, Gallery, Settings, Help

## @brief SampleApp creates the graphical user interface
#   and allows the window to switch between different frames.
#  @details the SampleApp contains the the start page,
#   display, gallery, settings, and help frames.


class SampleApp(tk.Tk):

    ## @brief Constructor for new app GUI object
    #  @details Creates object for GUI
    #  @param *args allows the function to accept an
    #         arbitrary number of arguments
    #  @param **kwargs allows the function
    #          to accept an arbitrary number of keyword arguments.
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for fr in (StartPage, Display.FlagDisplay,
                   Gallery.FlagGallery, Settings.Settings, Help.Help):
            page_name = fr.__name__
            frame = fr(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    ## @brief Shows the frame and switches between frames
    #  @details The frame is generated and switched.
    #  @param page_name Used to switch between frames in tkinter.
    #         The frame it will show on the window.
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

## @brief StartPage is a start page that opens once the program starts.
#         It displays the start page frame.
#  @details the StartPage contains buttons to start the flag generation,
#           chnage the settings,
#           open the gallery, and read the intructions.


class StartPage(Frame):
    ## @brief Creates the start page for the GUI main page.
    #  @details The start page will have the logo, start button,
    #           settings button, gallery button, and a help button.
    #  @param self Current object, common first parameter
    #         for any method of a class.
    #  @param parent A widget that acts as the parent of self, current object.
    #         All widgets in tkinter except the root window require a parent
    #  @param controller Other objects that are designed to act as a shared
    #         point, allowing several pages of widgets to interact. It
    #         decouples the different pages, making them independent. The
    #         controller decides what page will be visible.
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.image_app_logo = Image.open("./ImagesGUI/app_logo.png")
        self.image_start_button = Image.open("./ImagesGUI/start_button.png")
        self.image_gallery_button = Image.open(
            "./ImagesGUI/gallery_button.png")
        self.image_settings_button = Image.open(
            "./ImagesGUI/settings_button.png")
        self.image_help_button = Image.open("./ImagesGUI/help_button.png")


        self.resize_image_app_logo = self.image_app_logo.resize(
                                                                (512, 288))
        self.resize_image_start_button = self.image_start_button.resize(
                                                                (200, 100))
        self.resize_image_gallery_button = self.image_gallery_button.resize(
                                                                (200, 100))
        self.resize_image_settings_button = self.image_settings_button.resize(
                                                                (200, 100))
        self.resize_image_help_button = self.image_help_button.resize(
                                                                (200, 100))

        self.photo_app_logo = ImageTk.PhotoImage(
        self.resize_image_app_logo)
        self.photo_start_button = ImageTk.PhotoImage(
        self.resize_image_start_button)
        self.photo_gallery_button = ImageTk.PhotoImage(
        self.resize_image_gallery_button)
        self.photo_settings_button = ImageTk.PhotoImage(
        self.resize_image_settings_button)
        self.photo_help_button = ImageTk.PhotoImage(
        self.resize_image_help_button)



        self.app_logo = Label(self, image=self.photo_app_logo)

        self.start_button = Label(self, image=self.photo_start_button)
        self.start_generate = Button(self, image=self.photo_start_button,
                                     command=lambda: controller.show_frame
                                     ("FlagDisplay"))
        self.start_button.bind("<Button 1>",
                               lambda self: controller.show_frame
                               ("FlagDisplay"))

        self.gallery_button = Label(self, image=self.photo_gallery_button)
        self.gallery_generate = Button(self, image=self.photo_gallery_button,
                                       command=lambda: controller.show_frame
                                       ("FlagGallery"))
        self.gallery_button.bind("<Button 1>",
                                 lambda self: controller.show_frame
                                 ("FlagGallery"))

        self.settings_button = Label(self, image=self.photo_settings_button)
        self.settings_generate = Button(self, image=self.photo_settings_button,
                                        command=lambda: controller.show_frame
                                        ("Settings"))
        self.settings_button.bind("<Button 1>",
                                  lambda self: controller.show_frame
                                  ("Settings"))

        self.help_button = Label(self, image=self.photo_help_button)
        self.help_generate = Button(self, image=self.photo_help_button,
                                    command=lambda: controller.show_frame(
                                     "Help"))
        self.help_button.bind("<Button 1>",
                              lambda self: controller.show_frame("Help"))

        self.init_window()

    ## @brief Places the different widgets
    #         onto the start page for the GUI main page.
    #  @details The start page will include the logo, start button,
    #           settings button, gallery, and a help button.
    def init_window(self):
        self.app_logo.place(x=140, y=30)
        self.start_button.place(x=145, y=350)
        self.gallery_button.place(x=445, y=350)
        self.settings_button.place(x=145, y=475)
        self.help_button.place(x=445, y=475)


if __name__.endswith('__main__'):
    app = SampleApp()
    app.geometry("800x600")
    app.title("Flag Generator")
    app.mainloop()
