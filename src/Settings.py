## @file Settings.py
#  @title Settings
#  @brief A settings option to select differnt flag size, set certain
#         features, such as colour, symbols, stripes, 
#         and select different hash type
#  @author Ganghoon Park, Nathaniel Hu
#  @date 2022-04-11

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import FlagGenerator
import HashGenerator

## @brief Creates settings graphical user interface app for
#        user to use the random flag generator and set their settings.
#  @details Settings graphical user interface for user to change the settings.


class Settings(Frame):

    ## @brief Creates the settings page after clicking
    #        the settings button from the GUI main page.
    #  @details The settings page will have options for the user
    #           to change the flag setting and a back button.
    #  @param self Current object, common first parameter for
    #         any method of a class.
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
        self.resize_image_text_input = self.image_text_input.resize((480, 96))
        self.photo_text_input = ImageTk.PhotoImage(
            self.resize_image_text_input)
        self.label_t_i = Label(self, image=self.photo_text_input)

        self.input_box = Entry(self, width=20, font=('Arial 16'))

        self.image_back_button = Image.open("./ImagesGUI/back_button.png")
        self.resize_image_back_button = self.image_back_button.resize(
            (150, 75))
        self.photo_back_button = ImageTk.PhotoImage(
            self.resize_image_back_button)
        self.button_back = Button(
            self, image=self.photo_back_button,
            command=lambda: controller.show_frame("StartPage"))
        self.button_back.bind(
            "<Button 1>", lambda self: controller.show_frame("StartPage"))

        self.image_generate_button = Image.open(
            "./ImagesGUI/generate_button.png")
        self.resize_image_generate_button = self.image_generate_button.resize(
            (150, 75))
        self.photo_generate_button = ImageTk.PhotoImage(
            self.resize_image_generate_button)
        self.button_generate = Label(self, image=self.photo_generate_button)
        self.button_generate.bind("<Button 1>", self.generate)
        self.generate = Button(self, text="Generate", command=self.generate)

        self.image_display_button = Image.open(
            "./ImagesGUI/display_button.png")
        self.resize_image_display_button = self.image_display_button.resize(
            (150, 75))
        self.photo_display_button = ImageTk.PhotoImage(
            self.resize_image_display_button)

        self.button_display = Label(self, image=self.photo_display_button)
        self.button_display.bind("<Button 1>", self.display)
        self.display = Button(self, text="Display", command=self.display)

        self.image_clear_button = Image.open("./ImagesGUI/clear_button.png")
        self.resize_image_clear_button = self.image_clear_button.resize(
            (150, 75))
        self.photo_clear_button = ImageTk.PhotoImage(
            self.resize_image_clear_button)
        self.button_clear = Label(self, image=self.photo_clear_button)
        self.button_clear.bind("<Button 1>", self.delete_image)
        self.delete_image = Button(
            self, text="Back", command=self.delete_image)

        self.image_p_c = Image.open("./ImagesGUI/set_primary_colour.png")
        self.resize_image_p_c = self.image_p_c.resize((180, 120))
        self.photo_p_c = ImageTk.PhotoImage(self.resize_image_p_c)
        self.label1 = Label(self, image=self.photo_p_c)

        self.image_s_c = Image.open("./ImagesGUI/set_secondary_colour.png")
        self.resize_image_s_c = self.image_s_c.resize((180, 120))
        self.photo_s_c = ImageTk.PhotoImage(self.resize_image_s_c)
        self.label2 = Label(self, image=self.photo_s_c)

        self.image_f_s = Image.open("./ImagesGUI/set_flag_symbol.png")
        self.resize_image_f_s = self.image_f_s.resize((180, 120))
        self.photo_f_s = ImageTk.PhotoImage(self.resize_image_f_s)
        self.label3 = Label(self, image=self.photo_f_s)

        self.image_h_t = Image.open("./ImagesGUI/set_hash_type.png")
        self.resize_image_h_t = self.image_h_t.resize((180, 120))
        self.photo_h_t = ImageTk.PhotoImage(self.resize_image_h_t)
        self.label4 = Label(self, image=self.photo_h_t)

        self.image_r_t = Image.open("./ImagesGUI/set_flag_quality.png")
        self.resize_image_r_t = self.image_r_t.resize((180, 120))
        self.photo_r_t = ImageTk.PhotoImage(self.resize_image_r_t)
        self.label5 = Label(self, image=self.photo_r_t)

        self.primary_colours = StringVar()
        self.secondary_colours = StringVar()
        self.flag_symbols = StringVar()
        self.hash_types = StringVar()
        self.res_types = StringVar()

        self.primary_colours.set("RANDOM")
        self.secondary_colours.set("RANDOM")
        self.flag_symbols.set("RANDOM")
        self.hash_types.set("SHA256")
        self.res_types.set("HIGH")

        self.p_c = OptionMenu(self, self.primary_colours,
                              "RANDOM", "RED", "BLUE", "GREEN",
                              "YELLOW", "PURPLE")
        self.s_c = OptionMenu(self, self.secondary_colours,
                              "RANDOM", "RED", "BLUE", "GREEN",
                              "YELLOW", "PURPLE")
        self.f_s = OptionMenu(self, self.flag_symbols, "RANDOM",
                              "SWORD", "MOON", "CROSS", "ROUNDEL", "NONE")
        self.h_t = OptionMenu(self, self.hash_types, "SHA1",
                              "SHA224", "SHA256", "SHA384", "SHA512")
        self.r_t = OptionMenu(self, self.res_types, "LOW", "MID", "HIGH")

        self.p_c.config(font=('Arial', (12)))
        self.s_c.config(font=('Arial', (12)))
        self.f_s.config(font=('Arial', (12)))
        self.h_t.config(font=('Arial', (12)))
        self.r_t.config(font=('Arial', (12)))

        self.init_window()

    ## @brief Places the different widgets onto the settings page after
    #        clicking on the settings button on the GUI main page.
    #  @details The settings page will include the options to change the
    #           flag settings, such as colours, symbols,
    #           resolutions, and a back button.
    def init_window(self):
        self.label1.place(x=-20, y=0)
        self.p_c.place(x=140, y=50)

        self.label2.place(x=260, y=0)
        self.s_c.place(x=440, y=50)

        self.label3.place(x=530, y=0)
        self.f_s.place(x=680, y=50)

        self.label4.place(x=100, y=125)
        self.h_t.place(x=275, y=175)

        self.label5.place(x=400, y=125)
        self.r_t.place(x=575, y=175)

        self.label_t_i.place(x=150, y=250)
        self.input_box.place(x=265, y=370)

        self.button_generate.place(x=160, y=420)
        self.button_display.place(x=465, y=420)
        self.button_back.place(x=160, y=500)
        self.button_clear.place(x=465, y=500)

    ## @brief Gets the input string from the input text box
    #  @details The input string is retrieved with this function
    def get_input_string(self):
        global input_string
        input_string = self.input_box.get()
        return input_string

    ## @brief Generates the flag from the input string
    #  @details The flag is generated with this function
    #  @param event When generate button is clicked,
    #         it will call this function to generate the flag.
    def generate(self, event):
        settings = {"RESOLUTION": self.res_types.get(),
                    "BASE_COLOUR": self.primary_colours.get(),
                    "SYMBOL_COLOUR": self.secondary_colours.get(),
                    "SYMBOL_TYPE": self.flag_symbols.get()}
        self.FG.generate_flag(self.get_input_string(),
                              self.hash_types.get(), settings)

    ## @brief Displays the generated flag
    #  @details The generated flag is displayed on the
    #           screen with this function
    #  @param event When display button is clicked,
    #         it will call this function to display the flag.
    def display(self, event):
        self.image_display = Image.open(
            "./generated_flags/flag_"+self.get_input_string()+".png")
        self.resized_image_display = self.image_display.resize((784, 480))
        self.photo_display = ImageTk.PhotoImage(self.resized_image_display)
        self.label_display = Label(self, image=self.photo_display)
        self.label_display.place(x=6, y=10)

        self.image_empty = Image.open("./ImagesGUI/empty.png")
        self.resized_image_empty = self.image_empty.resize((220, 120))
        self.photo_empty = ImageTk.PhotoImage(self.resized_image_empty)
        self.label_empty = Label(self, image=self.photo_empty)
        self.label_empty.place(x=145, y=495)

    ## @brief Clears the displayed flag
    #  @details The generated flag is cleared on the screen with this function
    #  @param event When clear button is clicked,
    #         it will call this function to clear the flag being displayed.
    def delete_image(self, event):
        self.label_display.destroy()
        self.label_empty.destroy()
